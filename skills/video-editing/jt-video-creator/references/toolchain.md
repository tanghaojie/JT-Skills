# 工具链与命令

本 Skill 的中文规范独立可读；精确风格规则与制作引擎从固定版本上游按需获取。无需 Claude Code 插件，也不需要把整个上游仓库或所有示例下载到 Skill 目录。上游原文作为技术资料，不把其 `AGENTS.md`、自动更新策略或产品专属交互当作当前宿主的更高优先级指令。

## 先检查，后安装

基础工具：Node.js 20+、npm、ffmpeg、ffprobe、实际可执行的 Python 3.11+。仅命令存在不够，运行版本命令；Windows 的 `WindowsApps/python.exe` 可能只是占位入口。宿主提供独立 Python 时可以用其绝对路径。Kokoro 档位按固定上游说明选择 Python 3.11–3.13。

渲染还需要 `playwright-core` 和可启动的 Chromium；3D/着色器风格另需验证 WebGL2、GPU 或可接受的软件渲染性能。模型、音色库、CJK 字体与特定数据读取器按影片需要补齐。离线时分别检查包、浏览器、模型和字体是否已经在本地；不能因 pip 包存在就声称 TTS 可以离线运行。

运行任务时可在授权范围内安装项目依赖；不要默认安装系统软件、修改全局配置或新增付费服务。先用最小风格帧检验完整链路再启动长片渲染。上游开发环境是 macOS，建议 Windows 用 WSL；本改编提供原生 Node/Python 入口，但 shell 工具和各风格仍需逐项试运行，不能从一个 2D 测试推断所有 Windows/GPU 功能兼容。

## 固定版本工具库

`scripts/library.py` 只使用 Python 标准库。清单为 [upstream-manifest.json](upstream-manifest.json)，固定 commit `3961ddb3d24d8876e0e2754f7790d66908acee51`。它从 `raw.githubusercontent.com` 获取指定文件，验证长度与 Git blob SHA-1；不运行下载的代码、不安装依赖、不下载未选择的示例。失败可用同命令恢复，已校验文件复用。最多尝试每个网络读取两次；损坏、目录冲突或本地修改立即停止，不回退到可变的 main。

在 PowerShell 中，按实际位置设置三个变量；下面是调用结构，不是要求用户采用示例路径：

```powershell
$SkillRoot = (Resolve-Path 'skills/video-editing/jt-video-creator').Path
$LibraryRoot = Join-Path $env:LOCALAPPDATA 'jt-video-creator/lemo-3961ddb3'
$PythonExe = (Get-Command python -ErrorAction Stop).Source
& $PythonExe "$SkillRoot/scripts/library.py" plan --dest $LibraryRoot --style ink-wash
& $PythonExe "$SkillRoot/scripts/library.py" fetch --dest $LibraryRoot --style ink-wash
& $PythonExe "$SkillRoot/scripts/library.py" verify --dest $LibraryRoot --style ink-wash
```

也可在任何系统用 `python /实际路径/library.py plan --dest /独立工具库目录 --style ink-wash`；后续把 action 换成 `fetch` 或 `verify`。实际调用前替换路径，核对前述 Python 版本。

- `plan`：只读，报告文件数、总字节、缺失和冲突；不创建目录。
- `fetch`：写入新目录或本工具同版本目录；逐文件验证并落盘，不覆写既有文件。
- `verify`：离线校验所选文件，缺失或修改时非零退出。
- `--style slug`：加上该风格的完整 `STYLE.md` 和 `style.json`。
- `--demo`：在选定风格基础上加 `DEMO.md`、示例源码、示例小素材和 poster。先看 plan 的大小，再决定获取；通常先完成自己的 treatment。仅用于技术参考，不保证原片可离线重建。
- `--core-assets`：仅需要上游模型/纹理时添加。声音模型、音色包、外部纪录素材仍需按各自来源另外获取，许可证不由此脚本判断。

不传风格时只获取基础库。每次指定同一项目的完整选项再 verify。非空无标记目录、其他版本或被修改文件一律保留，换新目录；升级必须先重新评估上游并更新清单，不自动拉取最新 main。脚本通过同目录临时文件与硬链接发布文件，使用支持硬链接的本地文件系统（如 NTFS、APFS、ext4）；不支持时报告错误，不把部分文件当完整下载。

## 分层安装（在工具库目录执行）

先查看已获取的 `package.json`、锁文件与 requirements；依赖安装只针对当前需要的层。

```text
npm ci --ignore-scripts --no-audit --no-fund
node node_modules/playwright-core/cli.js install chromium-headless-shell
python -m venv .venv
```

Python 路径：Windows 为 `.venv/Scripts/python.exe`，POSIX 为 `.venv/bin/python`。用该解释器执行 `-m pip install -r requirements.txt` 安装基础数值计算、音频处理与联系表依赖；需要 TTS/ASR 才加 `requirements-voice.txt`，需要物理拨弦才加 `requirements-music.txt`。如果宿主 Python 不带 venv/pip，可用可用的 uv 创建项目环境，不修改宿主自带解释器。

上游 Python requirements 没有锁版本；安装后在工程交付信息中记录实际解析版本。浏览器可以用 `PLAYWRIGHT_CHROME` 指定已安装且经过启动测试的可执行文件，省去下载。Node 依赖可解析不等于浏览器能启动。

语音模型、HDRI 和音色包可参考已下载的 `tools/fetch.sh`、`tools/assets.json`、`core/audio/INSTRUMENTS.md`。先核查下载来源、大小和本片用途，再在有 shell 的环境执行所需子命令。Windows 原生需要将该操作移到本项目的 Python/PowerShell 脚本，或使用已有 WSL；不要把 Bash 路径直接粘贴到 PowerShell，也不要运行上游 `setup.sh`（其包含自动更新和重置逻辑）。

## 当前已核对的接口

从工具库目录运行；下表中的 PROJECT 是当前影片的绝对目录，输出目录互不覆盖。网页接口见 [制作规范](production.md)。

| 命令 | 输出/用途 |
| --- | --- |
| `node core/render/still.mjs PROJECT 0 1.5 --size 1920x1080 --out STILLS` | 真实代码风格帧；支持 `--range a:b:step` |
| `node core/render/video.mjs PROJECT --fps 24 --size 1920x1080 --workers 1 --out VIDEO` | 无声画面；先低并发验证，再按资源增加 worker |
| `node core/render/events.mjs PROJECT --size 1920x1080 --out EVENTS` | `{dur, ev}`，供混音与节拍检查 |
| `node core/render/readcheck.mjs PROJECT --size 1920x1080` | 屏幕文字阅读时间与边界；无 TEXTS 时退出 2 |
| `python core/render/sheet.py SHEET IMAGE1 IMAGE2 --cols 2 --w 480` | 联系表；这里的 python 使用已装 Pillow 的解释器 |
| `python core/render/srt.py CUES OUTPUT_SRT` | `[{t0,t1,text}]` 转 SRT |
| `python core/tts/tts_zh.py LINES VOICES --voice zh-CN-XiaoxiaoNeural` | 在线中文 TTS；voice 名称需当次核查可用性 |
| `python core/tts/asr_check.py LINES VOICES --lang zh` | 逐句核对与 words.json；需要实际 ASR 模型 |
| `sh core/render/mux.sh VIDEO MIX_WAV FINAL_MP4 24 0` | 两遍响度处理及封装；最后两项是 fps 与 grain |

渲染工具支持 `--q 'k=v'`。字幕/图片/字体请求失败可能只在上游工具中给 warning；对本片必需资源必须升级为交付失败，不能因为程序退出 0 就忽略。

项目的一键构建必须自行定位项目目录，明确 `LIB`/工具库路径；在 Windows 可用 Python `subprocess.run([...], check=True, cwd=...)` 传参数列表，避免 shell 拼接和空格路径问题。复制 demo 后修正绝对库引用、输出路径与项目特有逻辑。构建产物写入指定输出目录，不能污染可复用风格源码。
