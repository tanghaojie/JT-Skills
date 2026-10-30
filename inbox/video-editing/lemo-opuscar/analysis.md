# Lemo-Opuscar 分析与中文改编

## 原始请求

> $skill-creator 分析 https://github.com/lemomo-ai/lemo-opuscar 项目内容，复刻为中文的 jt-video-creator skill

整理结果：[jt-video-creator](../../../skills/video-editing/jt-video-creator/SKILL.md)。本次仅维护仓库源文件，不含全局安装、推送远程、发布插件或发布影片。

## 快照与来源

2026-10-22 通过 GitHub 连接器读取仓库、目录树、入口、指南、工具接口及代表风格。固定 commit 为 `3961ddb3d24d8876e0e2754f7790d66908acee51`，MIT，`Copyright (c) 2026 LemoLab`。完整归属与链接见 Skill 的 [来源说明](../../../skills/video-editing/jt-video-creator/references/sources.md)。

保留以下原文，`.source` 后缀用于避免把档案误当仓库指令或可调用 Skill：

- [Skill 入口](upstream/plugin__skills__lemo-opuscar__SKILL.md.source)
- [工作流 AGENTS](upstream/AGENTS.md.source)
- [导演指南](upstream/DIRECTOR.md.source)
- [技术指南](upstream/TECHNIQUE.md.source)
- [个人风格指南](upstream/MY-STYLES.md.source)
- [59 种风格索引](upstream/styles__README.md.source)
- [原始 setup.sh](upstream/plugin__skills__lemo-opuscar__scripts__setup.sh.source)
- [原始 MIT 许可](upstream/LICENSE.source)

原文未逐句改写；原文中的相对链接属于上游仓库，不是此收集目录的本地引用。分析以读取到的代码和文档为依据，没有把上游示例影片的宣传描述视作已独立验证的效果。

## 项目结构与值得复用的机制

| 层次 | 上游实现 | 复刻处理 |
| --- | --- | --- |
| 薄入口 | Skill 调 setup.sh，再委派给库内 AGENTS | 中文入口自含决策规则，明确工具库按需获取 |
| 导演 | 主题、treatment、风格帧、声音/节奏/镜头、审片 | 中文说明，保留创作先于 demo，数量约束按片型调整 |
| 风格资产 | 59 个 STYLE.md、style.json、DEMO.md 与示例工程 | 完整中文名称映射，选中后获取原文与所需示例 |
| 渲染 | 可随机访问的 render(t)、READY、DUR、EV、TEXTS；Playwright + ffmpeg | 保留实际 API，强调确定性、资源就绪、中文缺字和参数一致 |
| 声音 | edge-tts、Kokoro、Whisper、采样/合成/拨弦、混音封装 | 按联网/离线、用户录音和依赖条件选择，不静默替换 |
| 真实资料 | Evidence Films、Edit & Documentary、FACTS、素材登记 | 明确来源证据与画面权利分别记录，不伪造事实 |
| 个人风格 | 基础风格改造或空白创建，风格帧、测试片、保存和复用 | 中文草案与包格式，尊重已有授权，按用户指定位置保存 |
| 分发 | Claude 插件、main 自动更新、共享主目录 | 不搬运插件安装与 reset；使用锁定清单、安全增量下载 |

## 接口核查中发现的注意点

- 项目名称虽包含视频创作，但核心不是调用视频生成模型，而是代码画面与素材的确定性编排。
- `core/render/video.mjs` 才是实际视频入口，没有 `render.mjs`；README 的接口需与真实文件交叉核对。
- 当前依赖 `playwright-core`，其浏览器单独安装；仅 npm 安装成功不足以渲染。
- 默认画幅/fps 是起点，部分风格有不同参数。所有 still、video、events、readcheck 与 mux 必须一致。
- 上游中文字体只是约 200 字的子集，随意更换文本会缺字；应自托管覆盖当前文本的字体。
- 原生 Windows 可直接调用 Node/Python，但上游 shell 脚本和 GPU 不应未经验证就宣称兼容。
- 上游 setup.sh 含自动 fetch/reset 以及依赖目录重建；本次不直接沿用。
- 外部素材和字体许可不自动归入 MIT；公有领域和 CC0 也不是同一种许可记录。

## 验证记录

实际执行结果记录在 [validation.md](validation.md)，区分格式、脚本行为、渲染链路和未覆盖的视听/服务能力。
