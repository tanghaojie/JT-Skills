#!/usr/bin/env python3
"""按清单获取固定版本 Lemo-Opuscar；不安装依赖、不执行代码、不覆盖修改。"""

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import sys
import tempfile
import urllib.error
import urllib.request

MANIFEST = Path(__file__).resolve().parents[1] / 'references' / 'upstream-manifest.json'
MARKER = '.jt-video-library.json'


def blob_hash(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode('ascii') + b'\0' + data).hexdigest()


def manifest():
    data = json.loads(MANIFEST.read_text(encoding='utf-8'))
    if not re.fullmatch(r'[0-9a-f]{40}', data['commit']):
        raise ValueError('清单 commit 无效')
    seen = set()
    for item in data['files']:
        name = item['path']
        parts = PurePosixPath(name).parts
        if (not parts or name.startswith('/') or '\\' in name or ':' in name
                or any(p in ('.', '..') for p in name.split('/')) or name in seen):
            raise ValueError(f'清单路径无效或重复: {name}')
        if not re.fullmatch(r'[0-9a-f]{40}', item['sha']) or item['size'] < 0:
            raise ValueError(f'清单校验值无效: {name}')
        seen.add(name)
    return data


def select_files(data, style=None, demo=False, core_assets=False):
    slugs = {i['path'].split('/')[1] for i in data['files']
             if re.fullmatch(r'styles/[^/]+/STYLE.md', i['path'])}
    if style and style not in slugs:
        raise ValueError(f'未知风格 {style!r}；查阅 references/styles.md')
    if demo and not style:
        raise ValueError('--demo 必须同时指定 --style')
    selected = []
    for item in data['files']:
        path = item['path']
        if path.startswith('core/assets/'):
            include = core_assets
        elif path.startswith('styles/') and path != 'styles/README.md':
            prefix = f'styles/{style}/'
            include = bool(style and path.startswith(prefix) and (
                demo or path[len(prefix):] in ('STYLE.md', 'style.json')))
        else:
            include = True
        if include:
            selected.append(item)
    return selected


def target(root, name):
    path = root.joinpath(*PurePosixPath(name).parts)
    current = root
    for part in PurePosixPath(name).parts:
        current = current / part
        if current.is_symlink() or getattr(current, 'is_junction', lambda: False)():
            raise ValueError(f'拒绝通过符号链接或联接写入: {current}')
    if not path.resolve().is_relative_to(root):
        raise ValueError(f'路径越界: {name}')
    return path


def inspect(root, data, selected):
    if root.exists() and not root.is_dir():
        raise ValueError(f'目标不是目录: {root}')
    marker = target(root, MARKER)
    if marker.exists():
        info = json.loads(marker.read_text(encoding='utf-8'))
        if info.get('commit') != data['commit'] or info.get('repository') != data['repository']:
            raise ValueError('工具库版本或来源不同；请选择新目录，不覆盖现有库')
    elif root.exists() and any(root.iterdir()):
        raise ValueError('非空目录没有本工具标记；请指定新的独立目录')
    missing, conflicts = [], []
    for item in selected:
        path = target(root, item['path'])
        if not path.exists():
            missing.append(item)
        elif not path.is_file() or blob_hash(path.read_bytes()) != item['sha']:
            conflicts.append(item['path'])
    return missing, conflicts


def write_new(path, payload):
    """同目录临时文件经硬链接发布；目标若已出现则失败，不替换它。"""
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_name = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, prefix='.jt-download-', delete=False) as tmp:
            temp_name = tmp.name
            tmp.write(payload)
        os.link(temp_name, path)
    finally:
        if temp_name is not None:
            Path(temp_name).unlink(missing_ok=True)


def download(commit, item):
    url = f'https://raw.githubusercontent.com/lemomo-ai/lemo-opuscar/{commit}/{item["path"]}'
    request = urllib.request.Request(url, headers={'User-Agent': 'jt-video-creator/1'})
    for attempt in range(2):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                payload = response.read(item['size'] + 1)
            if len(payload) != item['size'] or blob_hash(payload) != item['sha']:
                raise ValueError(f'内容校验失败: {item["path"]}；没有写入该文件')
            return payload
        except (urllib.error.URLError, TimeoutError, OSError):
            if attempt:
                raise
    raise RuntimeError('下载未完成')


def run(args):
    data = manifest()
    selected = select_files(data, args.style, args.demo, args.core_assets)
    root = Path(args.dest).expanduser().resolve()
    missing, conflicts = inspect(root, data, selected)
    report = {
        'action': args.action, 'root': str(root), 'commit': data['commit'],
        'files': len(selected), 'bytes': sum(i['size'] for i in selected),
        'missing': len(missing), 'download_bytes': sum(i['size'] for i in missing),
        'conflicts': conflicts, 'style': args.style, 'demo': args.demo,
    }
    if conflicts:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        raise ValueError('发现本地修改；停止，不覆盖。保留该目录并使用新的工具库目录')
    if args.action == 'fetch':
        root.mkdir(parents=True, exist_ok=True)
        marker = target(root, MARKER)
        if not marker.exists():
            write_new(marker, (json.dumps({k: data[k] for k in ('repository', 'commit')}) + '\n').encode())
        for item in missing:
            payload = download(data['commit'], item)
            write_new(target(root, item['path']), payload)
            print(f'已获取 {item["path"]}', file=sys.stderr)
        remaining, conflicts = inspect(root, data, selected)
        if remaining or conflicts:
            raise ValueError('下载后的完整性检查失败')
        report['downloaded'] = len(missing)
        report['missing'] = 0
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if args.action == 'verify' and missing else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('plan', 'fetch', 'verify'))
    parser.add_argument('--dest', required=True, help='独立工具库目录；不使用已有普通项目目录')
    parser.add_argument('--style', help='风格 slug；不指定时只处理基础工具库')
    parser.add_argument('--demo', action='store_true', help='同时获取该风格示例源码和素材，仅读取参考')
    parser.add_argument('--core-assets', action='store_true', help='增加上游 core/assets 中的模型与纹理')
    args = parser.parse_args()
    try:
        return run(args)
    except (ValueError, KeyError, OSError, urllib.error.URLError) as exc:
        print(f'错误: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
