# JT-Skills 仓库约定

## 阅读入口

先读根目录 README.md，再读任务涉及的领域 README.md。新增或大幅调整 Skill 时，阅读 docs/adding-skills.md；只加载相关 Skill 和引用资料。

## 组织与维护

- 说明文档默认使用简体中文；目录及 Skill 名称使用小写英文、数字和连字符。
- 具体 Skill 放在 `skills/<领域>/<skill-name>/SKILL.md`，目录名与 frontmatter 的 `name` 一致，仓库内名称唯一。
- 新 Skill 建议使用 `jt-` 前缀；引入已有 Skill 时保留来源和必要署名，不为统一命名而抹去来源。
- 一个 Skill 对应一项可重复执行的任务。分类 README 不是 Skill，不要给它添加 Skill frontmatter。
- 每个 Skill 选择一个主要领域，跨领域关联通过索引链接表达，不复制多份实现。
- 原始提示词放在 inbox，整理时保留原文；在原文中记录整理结果的相对链接。
- 新增、移动或删除 Skill 后，更新所属领域 README 的索引及相关链接。
- 仅在实际需要时创建 scripts、references、assets 等资源目录。模板保留 `.template` 后缀，不作为可用 Skill 收录。
- 不把用户未提供的习惯、经历或工作流写成既定事实；具体任务中的临时条件不自动升级为通用规则。
- 仓库维护不默认包含安装到全局目录、发布插件、推送远程或修改外部服务。

## 完成前检查

确认名称与描述能区分相邻任务，所需输入和交付结果明确，引用路径有效，没有未替换的模板占位符。存在脚本时实际验证其行为；实际 Skill 应通过可用的格式校验，并说明行为试用覆盖范围。仅建立目录和模板时，无需声称已完成 Skill 行为验证。

<!-- CODEGRAPH_START -->
## CodeGraph

In repositories indexed by CodeGraph (a `.codegraph/` directory exists at the repo root), reach for it BEFORE grep/find or reading files when you need to understand or locate code:

- **MCP tool** (when available): `codegraph_explore` answers most code questions in one call — the relevant symbols' verbatim source plus the call paths between them, including dynamic-dispatch hops grep can't follow. Name a file or symbol in the query to read its current line-numbered source. If it's listed but deferred, load it by name via tool search.
- **Shell** (always works): `codegraph explore "<symbol names or question>"` prints the same output.

If there is no `.codegraph/` directory, skip CodeGraph entirely — indexing is the user's decision.
<!-- CODEGRAPH_END -->
