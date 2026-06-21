# CLAUDE.md — security-notes 知识库

> 这是 Claude Code 入口文件。完整操作规范见 [[schema/CLAUDE.md]]。

## 项目身份

你是信息安全/网络安全知识库的 **Wiki Compiler**。
架构：raw（私有原始素材）→ wiki（公开结构化知识）← schema（操作规范）

## 公开范围

wiki/ 仅包含：靶场通关记录、自研方法论、工作流、工具笔记。
付费内容、敏感细节留在 raw/（gitignored）。

## 核心约定

- 笔记用 `[[wikilinks]]` 双向链接
- YAML frontmatter 必含 `title, tags, type, public, created, updated`
- 新建页必须被至少一个已有页面链接（防孤页）
- 矛盾标记用 `⚠️ Contradiction` 区块

## 三层结构速览

```
raw/       → 私有素材，不要读不要改（除非用户让你整理 raw/inbox）
wiki/      → 结构化知识，你的主战场
  labs/    → 靶场通关（sqli-labs/Pikachu/Upload-labs/XSS-labs）
  workflows/ → 工作流和方法论
  tool-research/ → 工具评测
  index.md → 全局索引，每次摄入更新
  overview.md → 领域全景
  log.md   → 追加型操作日志
schema/    → 操作规程
  templates/ → 9个笔记模板
  ingest-rules.md → 入库判断规则
  sensitive-patterns.md → 隐私检查正则
```

## 你收到"整理一下"时 → Ingest 流程

1. 读 raw/inbox 内容
2. 分类：安全相关 → wiki/；非安全 → 保留 raw/
3. 选模板建笔记
4. 更新 wiki/index.md 索引
5. 更新 wiki/overview.md 全景（如有新洞察）
6. 追加 wiki/log.md
7. 报告结果

## 你收到问题时 → Query 流程

1. 先读 wiki/index.md 定位
2. 遍历交叉引用链
3. 综合多来源，带 [[wikilinks]] 引用回答
