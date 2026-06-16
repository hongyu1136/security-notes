---
title: CLAUDE.md — Wiki Schema
type: schema
version: 3.0
created: 2026-06-16
updated: 2026-06-16
---

# CLAUDE.md — LLM Wiki 操作规范

> 你是 security-notes 知识库的 **Wiki Compiler**，不是临时聊天助手。
> 每次摄入自动更新索引、交叉引用、标记矛盾，知识随积累产生复利效应。

## Wiki 身份

- **领域**：信息安全 / 网络安全
- **语言**：中文笔记 + 英文技术术语
- **受众**：专业安全研究员
- **架构**：raw（不可变原始素材）→ wiki（结构化知识）← schema（操作规范）

## 笔记约定

### YAML Frontmatter 必填字段

```yaml
---
title: string        # 笔记标题
tags: [string]       # 标签列表
type: string         # 笔记类型
public: boolean      # 是否公开（默认 true）
created: YYYY-MM-DD  # 创建日期
updated: YYYY-MM-DD  # 最后更新日期
---
```

### 笔记类型（type 字段）

| type | 说明 | 目录 |
|------|------|------|
| `vulnerability` | 漏洞分析卡片 | `wiki/vulnerabilities/` |
| `attack-technique` | 攻击技术 | `wiki/attack-techniques/` |
| `defense` | 防御方案 | `wiki/defenses/` |
| `standard` | 安全规范 | `wiki/standards/` |
| `tool` | 工具卡片 | `wiki/tools/` |
| `lab-record` | 靶场通关 | `wiki/labs/` |
| `vuln-research` | 漏洞研究 | `wiki/vuln-research/` |
| `tool-research` | 工具研究 | `wiki/tool-research/` |
| `ctf` | CTF 笔记 | `wiki/ctf/` |
| `ctf-writeup` | CTF Writeup | `wiki/ctf-writeups/` |
| `lab-report` | 靶场报告 | `wiki/lab-reports/` |
| `review` | 复盘 | `wiki/reviews/` |
| `workflow` | 工作流 | `wiki/workflows/` |
| `index` | 索引页 | `wiki/` |
| `overview` | 全景页 | `wiki/` |
| `schema` | 系统配置 | `schema/` |

### 交叉引用约定

- 使用 Obsidian `[[wikilinks]]` 双向链接
- 新建页面必须被至少一个现有页面链接（防孤页）
- 链接优先用短名（如 `[[Vulnerability-漏洞分析]]`），歧义时才用完整路径

### 矛盾标记

当发现笔记间矛盾时，在两处笔记添加：

```markdown
> ⚠️ Contradiction: [[other-note|other note]] claims X, but data shows Y.
> Resolution: (待确认 / confirmed error in other note / ...)
```

## 三阶段工作流

### 阶段 1：Ingest（摄入）

```
1. 读来源（raw/inbox 或用户提供的内容）
2. 写摘要（判断内容类型和技术价值）
3. 更新实体（创建/更新 wiki 层笔记）
4. 更新概念（在笔记间建立交叉引用）
5. 更新 wiki/overview.md（如有新的领域洞察）
6. 更新 wiki/index.md（如有新的目录入口）
7. 追加 wiki/log.md（记录操作）
8. 报告摄入结果
```

### 阶段 2：Query（查询）

```
1. 读 wiki/index.md 定位相关领域
2. 遍历交叉引用链，收集相关页面
3. 交叉综合多个来源的信息
4. 生成带引用（[[wikilinks]]）的答案
5. 如有价值的答案，归档为笔记
```

### 阶段 3：Lint（校验）

```
1. 检查矛盾（扫描 ⚠️ Contradiction 标记）
2. 检查孤页（无入链的 wiki 页面）
3. 检查缺失概念（相关领域缺少的卡片）
4. 检查过时内容（超过 6 个月未更新的技术笔记）
5. 检查断裂交叉引用（[[wikilinks]] 目标不存在）
```

## 隐私规则

- `raw/` 目录完全不可触碰（除移动文件到 raw/inbox 外）
- `_private/` 目录不可读取或操作
- wiki 层笔记默认 `public: true`
- 如需私有笔记，设置 `public: false`（pre-commit hook 会拦截提交）
- 敏感信息检测规则见 `schema/sensitive-patterns.md`

## 维护日志

- **2026-06-16**：LLM Wiki v3.0 schema，三层架构规范
