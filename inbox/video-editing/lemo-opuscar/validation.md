# 验证记录

日期：2026-10-22。目标：[jt-video-creator](../../../skills/video-editing/jt-video-creator/SKILL.md)。没有安装为全局 Skill、推送远程或发布影片。

## 格式与静态检查

- 使用当前 `skill-creator/scripts/quick_validate.py` 验证，输出 `Skill is valid!`。Python 使用 Codex 工作区运行时，PyYAML 复用仓库已有 `.venv/skill-check`；未修改全局 Python。
- YAML 名称与目录一致，仓库 Skill 名称唯一；`agents/openai.yaml` 短说明长度和默认提示中的调用名称有效。
- 本地 Markdown 链接已检查；`.source` 原始档案里的上游相对引用不作为本地链接检查。
- 中文风格目录与固定清单一一匹配，共 59 个唯一 slug；清单保存 1,981 个可按需获取的上游文件条目，不代表已下载全部条目。
- 关键原文快照与上游 Git blob 哈希匹配，MIT 声明完整保留；无未完成的 Skill 模板占位符。

## 下载脚本

隔离目录：`C:/Users/thj_3/AppData/Local/Temp/jt-video-creator-validation-20261022/`。

实际调用 `library.py`：

1. `plan --style swiss-motion` 报告 47 个文件、475,683 字节，且不创建下载目录。
2. `fetch --style swiss-motion` 成功获取并验证全部 47 个文件。
3. 相同命令再次运行：下载 0 个文件、0 字节。
4. `--demo` 增量获取 24 个文件、316,748 字节；合计 71 个文件、792,431 字节。
5. 所选文件完成离线完整性校验。依赖安装后仍能核验原始源码；node_modules 不属于上游源码校验对象。

另外使用标准库 unittest 运行 10 项行为测试，全部通过：只读计划/缺失验证不建目录、增量/幂等/离线校验、修改文件保留、非空普通目录保留、其他版本保留、未知风格及 demo 参数拒绝、路径越界拒绝、内容损坏不发布、网络尝试有界、既有目标不覆盖。测试脚本位于上述隔离目录 `test_library.py`；测试数据没有进入工作树。

## 实际渲染冒烟测试

在固定上游库中用 `npm ci --ignore-scripts` 安装两项锁定 Node 依赖，使用本机 Chrome；没有运行上游 setup.sh。测试工程目录名称含中文和空格：`中文路径 smoke/`，从工程之外调用 `build.py --out .../output-a`。

- 环境：Windows，Node 24.19.0、ffmpeg 8.0、Chrome 154.0.8037.98。
- 工程：原创最小 Canvas 页面，中文标题、移动矩形、确定性 render(t)、DUR/READY/EV/TEXTS 接口。
- 通过真实 `still.mjs`、`events.mjs`、`readcheck.mjs`、`video.mjs`；Windows 用测试工程 Python 调用 ffmpeg 完成测试正弦音与两遍 loudnorm 封装。
- 输出：6.000 秒、320×180、24 fps、144 帧、H.264 视频与 48 kHz AAC 音频。
- 全文件解码通过，blackdetect 无黑场；ebur128 测得 −14.0 LUFS，真峰值测得 −9.8 dBFS。
- 视觉检查了 1.5 秒截图：中文无缺字，图形清晰且在边界内。
- 独立再次启动浏览器，按反向顺序渲染 5.9、1.5、0 秒；三个 JPEG 与首次相同时间点逐字节一致。
- 成片及证据保留在隔离目录的 `output-a/`，包括 `smoke.mp4`、`ffprobe.json`、`checks.txt` 和 `stills/`。这是接口冒烟测试，不是瑞士动态排版风格的质量样片。

## 独立行为试用

按 skill-creator 的 Independent Forward-Testing，由独立子代理在隔离目录 `C:/Users/thj_3/AppData/Local/Temp/jt-video-creator-forward-20261022/` 试用；仅提供 Skill 与真实任务，不预告期望答案。该试用禁止联网、安装、渲染和修改仓库。

| 请求 | 观察到的结果 |
| --- | --- |
| 20 秒竖屏中文留存率新闻；20% 到 25%，样本量缺失；无配音、离线、只要方案、风格自定 | 生成 TREATMENT、FACTS、连续 0–20 秒 timeline；保留用户约束，正确写增加 5 个百分点，不虚构显著性或原因，不生成假成片路径 |
| 对缺失的现有 MP4 去掉前 3 秒并转 720p | 识别为普通裁剪转码，未进入风格导演流程，确认文件缺失并说明实际阻塞 |

试用暴露了离线时完整 STYLE.md 缺失的表述空间，已在入口追加：可继续交付“风格待核验”的方案，不宣称风格已复现。

## 未验证与限制

- 未制作真实用户主题的正式成片，未逐一渲染 59 种风格。
- 未调用在线 edge-tts、Kokoro、Whisper 或下载音色/模型；未做真实人声、配乐和完整视听验收。
- 未验证 3D/GPU、所有平台画幅、外部资料抓取、上游 Bash 封装或个人风格包的保存重建。
- 下载测试覆盖基础库和一个风格的 demo，不证明清单内每项远程文件在未来都能访问。
- 本次读取 agent-reach 的 GitHub 路由后使用已连接 GitHub 工具；本机没有可执行的 `agent-reach` 命令，因此未能检查其更新。这不影响上游源代码读取与上述测试。
