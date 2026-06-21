# security-notes — LLM Wiki 安全知识库

信息安全/网络安全学习与研究的 Obsidian Vault，采用 [Andrej Karpathy LLM Wiki](https://github.com/karpathy/llm-wiki) 三层架构。

## 公开范围

**wiki/ 层仅包含**：靶场通关记录、自研方法论、工作流、工具笔记。
**不包含**：知识星球/付费社区内容、未授权渗透细节、他人版权材料。

## 三层架构

| 层级 | 目录 | Git | 职责 |
|------|------|-----|------|
| **raw/** | 原始素材 | ❌ gitignored | 临时收集、旧资料导入，LLM 不直接操作 |
| **wiki/** | 结构化知识 | ✅ 公开提交 | LLM 操作的结构化笔记，每次摄入更新索引 |
| **schema/** | 操作规范 | ✅ 公开提交 | CLAUDE.md、入库规则、模板、敏感信息检测 |

## 快速导航

- **全局索引**：[[wiki/index|Wiki Index]] — 符号表、目录、模板入口
- **领域全景**：[[wiki/overview|Overview]] — 安全领域知识全景
- **操作日志**：[[wiki/log|Operation Log]] — 追加型 Lambda Lab 式日志
- **入库规则**：[[schema/ingest-rules|Ingest Rules]] — Codex 入库判断流程

## Wiki 层结构

| 目录 | 内容 |
|------|------|
| `wiki/vulnerabilities/` | 漏洞卡片（CVE/CNVD 分析） |
| `wiki/attack-techniques/` | 攻击技术（MITRE ATT&CK） |
| `wiki/defenses/` | 防御方案 |
| `wiki/standards/` | 安全规范 |
| `wiki/tools/` | 工具卡片 |
| `wiki/labs/` | 靶场通关记录（sqli-labs, Pikachu, Upload-labs, XSS-labs） |
| `wiki/vuln-research/` | 漏洞深度研究 |
| `wiki/tool-research/` | 工具评测与研究 |
| `wiki/ctf/` | CTF 比赛笔记 |
| `wiki/ctf-writeups/` | CTF Writeup 成品 |
| `wiki/lab-reports/` | 靶场报告 |
| `wiki/reviews/` | 定期复盘（日/周/月） |
| `wiki/workflows/` | 可复用工作流（信息收集/漏洞挖掘/渗透测试/应急响应） |

## 模板

| 模板 | 用途 |
|------|------|
| [[schema/templates/Vulnerability-漏洞分析|Vulnerability-漏洞分析]] | CVE/CNVD 漏洞分析 |
| [[schema/templates/Attack-攻击技术|Attack-攻击技术]] | MITRE ATT&CK 攻击技术 |
| [[schema/templates/Tool-工具卡片|Tool-工具卡片]] | 安全工具记录 |
| [[schema/templates/Lab-靶场通关|Lab-靶场通关]] | 靶场实验记录 |
| [[schema/templates/CTF-Writeup|CTF-Writeup]] | CTF 比赛记录 |
| [[schema/templates/Knowledge-知识卡片|Knowledge-知识卡片]] | 通用知识沉淀 |
| [[schema/templates/Inbox-待处理|Inbox-待处理]] | 新资料收集 |
| [[schema/templates/Topic-选题|Topic-选题]] | 研究选题 |
| [[schema/templates/Review-复盘|Review-复盘]] | 定期复盘 |

## 三阶段工作流

1. **Ingest**：读来源 → 写摘要 → 更新实体/概念 → 更新 overview → 更新 index → 追加 log → 报告
2. **Query**：读 index → 定位相关页 → 交叉综合 → 生成带引用答案
3. **Lint**：查矛盾、查孤页、查缺失概念、查过时内容、查断裂交叉引用

## 隐私策略

- `raw/` 整个目录 gitignored（个人上下文，不公开）
- `wiki/` 默认公开，个别笔记可标记 `public: false`
- Pre-commit hook 拦截 `public: false` 文件提交

## 维护日志

- **2026-06-16**：重构为 LLM Wiki 三层架构（raw/wiki/schema）
- **2026-06-02**：初始化知识库结构，添加安全领域模板和分类体系
