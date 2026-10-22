# 来源、版本与改编说明

整理日期：2026-10-21。此文件用于维护溯源，日常评审无需联网读取原文。三个来源已在本次创建中读取；评分机制由 jt-ai-check 新增。

## 1. dontbesilent：dbs-ai-check

- 作者：dontbesilent / dontbesilent2025。
- [固定版本原文](https://github.com/dontbesilent2025/dbskill/blob/14b567fc71beef647d52a6bc40a4e9b71a9ee6c5/skills/dbs-ai-check/SKILL.md)。提交：`14b567fc71beef647d52a6bc40a4e9b71a9ee6c5`；文件 blob：`97ce1d93c45c882cd12871bc57ae1eb72816a388`。
- [该提交的 LICENSE](https://github.com/dontbesilent2025/dbskill/blob/14b567fc71beef647d52a6bc40a4e9b71a9ee6c5/LICENSE) 声明：Copyright (c) 2026 dontbesilent，采用 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)。改编部分保留此署名、来源及非商业许可约束，不宣称获得商业再许可。
- 采用：默认诊断、按原文顺序举证、22 个模式方向、体裁误伤控制。
- 修改：22 个方向重新表述为上下文线索；删除“强信号几乎只有 AI”及“完美就不真实”的推断；不继承对用户的训诫、dbs 路由或强制逐条问答。增加明确评分、去重、缺项、JT 适配与只读交付规则。

## 2. 飞书：《【AI写作】4招去除写作AI味儿》

- [用户指定页面](https://vupyskvyxk.feishu.cn/wiki/SIXJw0q7nihzEDkOPnFckkXYnF8)。页面自述作者为“大师”，可见空间名“🔥大师的AI小灶”。
- 通过用户指定浏览器标签页读取完整可见正文。页面显示“1月2日修改”，没有可确认年份；不是不可变版本链接。
- 采用概念：表达不必机械整齐；作者身份、受众和任务应协调；真实记忆与立场可构成作者声音。
- 取舍：不复制原文提示词和个人经历示例；不使用 MBTI 推断 JT 人格，不通过补造犹豫、情绪、经历来提高分数，不引用未经核验的认知科学主张作为检测理论。
- 可见正文未发现明确转载许可。本文件记录来源及概念参考，不表示取得全文再分发许可。

## 3. 用户指定的 jt-humanizer-zh

- 本地来源：`C:/Users/thj_3/Desktop/posts/skills/jt-humanizer-zh/SKILL.md`。
- 读取日期：2026-10-21；SHA-256：`5B99CC1E14A415DF59547448BD8394A4FB2DC3D9C8D081EF272DCA056D8B6A06`。
- 采用：五条硬性规则、六条结构规则、两条句式规则、作者声音与事实归属约束、五维 50 分的质量方向。
- 修改：将“执行改写”变成“识别偏离并评分”；不继承原项目的绝对路径依赖、强制读取全部 JT/S 文档、文章版本命名或发布排版流程。本 Skill 的报告不是代 JT 写作。
- 本次没有另外读取作者确认终稿或 JT/S 文档，因此风格基线只声称来自该 Skill，不代表已完成所有个人写作样本的校准。

## 新增设计

AI 味五维权重、0–4 锚点、0–100 分档、60% 评分覆盖门槛、JT 扣分方式、证据去重与校准案例均为本 Skill 新增的维护约定，不是上述作者的原话或公认检测标准。

规则冲突时采用：用户当前要求 → 适用任务规范 → 本 Skill 的 JT 个人风格基线 → 通用模式提示。保留可读性与信息完整性，不靠删除事实条件或伪造个人化材料制造“人味”。
