# 来源、许可与改编边界

- 上游：[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)，作者 Lemomo / LemoLab。
- 核对日期：2026-10-22。
- 固定提交：[`3961ddb3d24d8876e0e2754f7790d66908acee51`](https://github.com/lemomo-ai/lemo-opuscar/commit/3961ddb3d24d8876e0e2754f7790d66908acee51)。该快照的风格索引含 59 种；不宣称未来数量不变。
- 上游代码和文档按 MIT 提供，版权声明为 `Copyright (c) 2026 LemoLab`；本目录保留完整 [LICENSE](../LICENSE)。中文改写并不消除原署名。外部素材、字体、音色和模型仍分别遵守其许可。

## 来源映射

以下链接都锁定同一提交；不需要每次启动全部读取。

| 上游 | 此 Skill 中的对应内容 |
| --- | --- |
| [Skill 入口](https://github.com/lemomo-ai/lemo-opuscar/blob/3961ddb3d24d8876e0e2754f7790d66908acee51/plugin/skills/lemo-opuscar/SKILL.md)、[AGENTS](https://github.com/lemomo-ai/lemo-opuscar/blob/3961ddb3d24d8876e0e2754f7790d66908acee51/AGENTS.md) | 中文入口、风格和故事分离、独立项目目录、按需路由 |
| [DIRECTOR](https://github.com/lemomo-ai/lemo-opuscar/blob/3961ddb3d24d8876e0e2754f7790d66908acee51/DIRECTOR.md) | [导演规范](directing.md)、[验收](quality.md) |
| [TECHNIQUE](https://github.com/lemomo-ai/lemo-opuscar/blob/3961ddb3d24d8876e0e2754f7790d66908acee51/TECHNIQUE.md)、[core 命令](https://github.com/lemomo-ai/lemo-opuscar/blob/3961ddb3d24d8876e0e2754f7790d66908acee51/core/README.md) | [制作规范](production.md)、[工具链](toolchain.md)，工具接口依据实际脚本交叉核对 |
| [MY-STYLES](https://github.com/lemomo-ai/lemo-opuscar/blob/3961ddb3d24d8876e0e2754f7790d66908acee51/MY-STYLES.md) | [个人风格](custom-styles.md) |
| [styles 索引](https://github.com/lemomo-ai/lemo-opuscar/blob/3961ddb3d24d8876e0e2754f7790d66908acee51/styles/README.md) | [中文风格目录](styles.md)，保持 59 个名称与 slug 一一对应 |
| [setup.sh](https://github.com/lemomo-ai/lemo-opuscar/blob/3961ddb3d24d8876e0e2754f7790d66908acee51/plugin/skills/lemo-opuscar/scripts/setup.sh) | 参考其分层获取思路，重新编写 [library.py](../scripts/library.py)，不执行上游自动更新逻辑 |

## 有意调整

- 中文入口、文档与默认沟通；不再先问语言。用当前宿主提供的提问能力，不依赖 Claude 的 `AskUserQuestion`。
- 保留普通影片、实证/纪实、个人风格三条路径。制作范围由用户任务决定；只要求方案时止于方案，不强行渲染。
- 精确风格提示词与引擎保留上游原文并按需获取，未宣称全文翻译了 59 份提示词。使用时把选中风格的适用规则转成中文方案，避免一次加载整座风格库。
- 工具库不自动更新或 reset；固定 commit、文件哈希与字节数，拒绝覆盖本地修改；不默认往主目录安装或写个人风格。
- 上游的固定访谈、反复批准和镜头数量改成按任务需要采用。用户要求先审片时尊重该节点，已经授权自主执行时不重复索要同一许可。
- 上游“无素材视频”的总述与后来新增的真实档案剪辑路径不完全一致；此处明确代码动画与真实素材编排都支持，真实资料不由生成画面替代。
- 上游宣称风格针对特定 Claude 模型调优，这是作者的适配说明，不是本 Skill 在其他模型上的效果保证。当前实际检查范围见仓库中的分析与验证记录；格式通过不能推断 59 种成片都已验收。
