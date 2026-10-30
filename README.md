# JT-Skills

把重复使用的提示词整理成可复用、可维护的个人 Skill 库。

按领域查找，按具体任务建立 Skill。一个 Skill 聚焦一个清晰的交付结果，例如「公众号文章改写」「建筑模型验收」「视频字幕校对」，避免把整个领域塞进一个入口。

## 分类导航

| 领域 | 目录 | 适合收录的任务 |
| --- | --- | --- |
| 写作 | [writing](skills/writing/README.md) | 选题、资料整理、文章写作、改写、标题、内容审校 |
| 三维建模 | [3d-modeling](skills/3d-modeling/README.md) | 参考资料、建模、材质灯光、动画、模型导出与验收 |
| 软件开发 | [software-development](skills/software-development/README.md) | 需求分析、架构设计、功能开发、调试、测试、代码审查与发布 |
| 视频剪辑 | [video-editing](skills/video-editing/README.md) | 素材整理、粗剪、字幕、音频、包装、导出与验收 |
| 文档处理 | [document-processing](skills/document-processing/README.md) | Word、PDF、表格、演示文稿、格式转换与批量处理 |
| 金融 | [finance](skills/finance/README.md) | 金融资料核验、A 股盘前准备、行情观察、市场复盘与交易复盘 |
| 跨领域通用 | [shared](skills/shared/README.md) | 多个领域共同使用的资料核验、需求澄清、交付检查 |

## 目录结构

```text
JT-Skills/
├── README.md                   分类导航与使用入口
├── AGENTS.md                   AI 维护此仓库的约定
├── skills/
│   ├── writing/
│   ├── 3d-modeling/
│   ├── software-development/
│   ├── video-editing/
│   ├── document-processing/
│   ├── finance/
│   └── shared/
├── inbox/                      尚未整理成 Skill 的原始提示词与资料
│   └── finance/                金融原始材料、核对记录与拆分评估
├── templates/
│   ├── SKILL.md.template       新 Skill 模板
│   └── prompt.md.template      原始提示词收集模板
└── docs/
    └── adding-skills.md        从提示词到 Skill 的整理方法
```

每个领域目录里的 README 是分类说明与索引；具体 Skill 放在它的下一层。已收录：[jt-ai-check](skills/writing/jt-ai-check/SKILL.md)，用于评判 AI 味与 JT 风格适配度，默认只打分、不改写；[jt-model](skills/3d-modeling/jt-model/SKILL.md)，用于复用项目要求、检查工具并完成三维模型交付。

金融领域已收录：[jt-stock-review](skills/finance/jt-stock-review/SKILL.md)，按大盘、板块、个股完成盘后复盘；[jt-stock-intraday](skills/finance/jt-stock-intraday/SKILL.md)，按相同层级完成盘前准备、集合竞价和盘中时点分析。

视频领域已收录：[jt-video-creator](skills/video-editing/jt-video-creator/SKILL.md)，将主题或真实资料制作成中文风格短片，支持 59 种上游风格检索、个人风格复用与可重建工程交付。

## 开始使用

1. 把常用提示词放入 [inbox](inbox/README.md)，可以直接保存，也可以使用[收集模板](templates/prompt.md.template)。
2. 依据[添加指南](docs/adding-skills.md)，把一个重复任务整理成独立 Skill。
3. 用真实任务试用，更新所属领域的「已收录 Skill」索引。

也可以直接让 AI 整理：

> 请把 inbox 中这份提示词整理成写作领域的 Skill，遵循本仓库 AGENTS.md 和添加指南，保留原始材料，并更新分类索引。

本仓库是 Skill 源文件库。领域分类目录用于管理，不代表宿主已经安装或能自动发现其中的 Skill。后续接入 Codex 或其他工具时，应按目标宿主的安装方式接入具体 Skill 文件夹；仓库内存放不等于安装完成。
