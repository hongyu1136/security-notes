---
title: Wiki Index
type: index
public: true
created: 2026-06-16
updated: 2026-06-16
---

# Wiki Index — 安全知识库全局索引

> LLM Wiki 架构：raw（原始素材）→ wiki（结构化知识）← schema（操作规范）

## 快速入口

- [[README]]
- [[schema/ingest-rules|Codex 入库规则]]
- [[wiki/overview|领域全景]]
- [[wiki/log|操作日志]]

## Wiki 层目录

### 漏洞与攻击
- `wiki/vulnerabilities/` — 漏洞卡片（CVE/CNVD 分析、复现记录）
- `wiki/attack-techniques/` — 攻击技术（MITRE ATT&CK 映射）
- `wiki/defenses/` — 防御方案
- `wiki/standards/` — 安全规范

### 工具与靶场
- `wiki/tools/` — 工具卡片
- `wiki/labs/` — 靶场通关记录
  - [[wiki/labs/sqli-labs/|sqli-labs]] · [[wiki/labs/pikachu靶场通关/|Pikachu]] · [[wiki/labs/upload-labs靶场通关/|Upload-labs]] · [[wiki/labs/xxs-labs通关/|XSS-labs]]
- `wiki/tool-research/` — 工具评测与研究
  - [[wiki/tool-research/ai-pentest-agent-architecture|AI 渗透 Agent 架构]] — 腾讯云黑客松十强方案拆解

### 研究与竞赛
- `wiki/vuln-research/` — 漏洞深度研究
- `wiki/ctf/` — CTF 比赛笔记
- `wiki/ctf-writeups/` — CTF Writeup 成品
- `wiki/lab-reports/` — 靶场报告

### 复盘与工作流
- `wiki/reviews/` — 定期复盘（日/周/月）
- `wiki/workflows/` — 可复用工作流
  - [[wiki/workflows/信息收集/信息收集流程|信息收集]] · [[wiki/workflows/漏洞挖掘/漏洞挖掘流程|漏洞挖掘]] · [[wiki/workflows/渗透测试/渗透测试流程|渗透测试]] · [[wiki/workflows/应急响应/应急响应流程|应急响应]] · [[wiki/workflows/报告撰写/报告撰写流程|报告撰写]]
  - [[wiki/workflows/ai-skills-methodology|AI Skills 方法论]] — 用 AI 辅助安全研究

## 模板入口

- [[schema/templates/Inbox-待处理|Inbox 模板]] — 新资料收集
- [[schema/templates/Knowledge-知识卡片|知识卡片模板]] — 通用知识沉淀
- [[schema/templates/Vulnerability-漏洞分析|漏洞分析模板]] — CVE/CNVD 漏洞分析
- [[schema/templates/Attack-攻击技术|攻击技术模板]] — MITRE ATT&CK 映射
- [[schema/templates/Tool-工具卡片|工具卡片模板]] — 安全工具记录
- [[schema/templates/Lab-靶场通关|靶场通关模板]] — 靶场实验记录
- [[schema/templates/CTF-Writeup|CTF Writeup 模板]] — CTF 比赛记录
- [[schema/templates/Topic-选题|选题模板]] — 研究选题
- [[schema/templates/Review-复盘|复盘模板]] — 定期复盘

## Raw 层（私有）
- `raw/inbox/` — 临时收集、待处理
- `raw/legacy/` — 旧资料导入

## 安全领域分类参考

### OWASP Top 10 (2021)
1. A01:Broken Access Control - 失效的访问控制
2. A02:Cryptographic Failures - 加密机制失效
3. A03:Injection - 注入
4. A04:Insecure Design - 不安全设计
5. A05:Security Misconfiguration - 安全配置错误
6. A06:Vulnerable and Outdated Components - 组件漏洞
7. A07:Identification and Authentication Failures - 认证失败
8. A08:Software and Data Integrity Failures - 软件和数据完整性失败
9. A09:Security Logging and Monitoring Failures - 安全日志监控失败
10. A10:Server-Side Request Forgery (SSRF) - 服务端请求伪造

### MITRE ATT&CK 攻击阶段
1. Reconnaissance - 侦察
2. Resource Development - 资源开发
3. Initial Access - 初始访问
4. Execution - 执行
5. Persistence - 持久化
6. Privilege Escalation - 权限提升
7. Defense Evasion - 防御规避
8. Credential Access - 凭据访问
9. Discovery - 发现
10. Lateral Movement - 横向移动
11. Collection - 收集
12. Command and Control - 命令控制
13. Exfiltration - 数据窃取
14. Impact - 影响
