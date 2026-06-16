---
title: Security Knowledge Overview
type: overview
public: true
created: 2026-06-16
updated: 2026-06-16
---

# 安全知识全景

> 信息安全/网络安全领域的结构化知识全景，随摄入持续更新。

## 当前重点领域

### Web 安全
- **SQL 注入**：sqli-labs 1-30 关通关，覆盖联合查询、报错注入、布尔盲注、时间盲注、堆叠注入、宽字节注入、HTTP 头注入、二次注入、WAF 绕过
  - [[wiki/labs/sqli-labs-25-30-summary|Less 25-30 总结]]
- **XSS**：xss-labs 进行中，Pikachu 反射/存储/DOM 型完成
- **文件上传**：upload-labs pass-1 至 pass-21 通关
- **CSRF / SSRF / XXE / RCE / 文件包含**：Pikachu 靶场完成
- **暴力破解 / 越权 / 信息泄露 / URL 重定向**：Pikachu 靶场完成

### 工具链
- Docker 部署（Vulhub、Pikachu、DVWA）
  - [[wiki/tool-research/docker/部署vulhub|部署 Vulhub]]
  - [[wiki/tool-research/docker/部署经典靶场（pikachu、dvwa等）|部署经典靶场]]

### 靶场进度

| 靶场 | 进度 | 目录 |
|------|------|------|
| sqli-labs | 30/65 关 | [[wiki/labs/sqli-labs/]] |
| Pikachu | 全部完成 | [[wiki/labs/pikachu靶场通关/]] |
| Upload-labs | 21/21 关 | [[wiki/labs/upload-labs靶场通关/]] |
| XSS-labs | 进行中 | [[wiki/labs/xxs-labs通关/]] |
| DVWA | 待开始 | — |

### 工作流
- [[wiki/workflows/信息收集/信息收集流程|信息收集]]
- [[wiki/workflows/漏洞挖掘/漏洞挖掘流程|漏洞挖掘]]
- [[wiki/workflows/渗透测试/渗透测试流程|渗透测试]]
- [[wiki/workflows/应急响应/应急响应流程|应急响应]]
- [[wiki/workflows/报告撰写/报告撰写流程|报告撰写]]

## OWASP Top 10 覆盖

| # | 类别 | 靶场覆盖 | 研究深度 |
|---|------|---------|---------|
| A01 | Broken Access Control | Pikachu（越权） | 基础 |
| A02 | Cryptographic Failures | — | 待补充 |
| A03 | Injection | sqli-labs 30关 | 较深 |
| A04 | Insecure Design | — | 待补充 |
| A05 | Security Misconfiguration | — | 待补充 |
| A06 | Vulnerable Components | — | 待补充 |
| A07 | Auth Failures | Pikachu（暴力破解） | 基础 |
| A08 | Software Integrity Failures | Upload-labs | 中等 |
| A09 | Logging/Monitoring Failures | — | 待补充 |
| A10 | SSRF | Pikachu | 基础 |

## 待探索方向

- [ ] 内网渗透 / 域渗透
- [ ] 云安全（AWS/Azure/GCP）
- [ ] 移动安全（Android/iOS）
- [ ] 逆向工程 / 二进制漏洞
- [ ] 密码学攻击
- [ ] 安全开发（SAST/DAST/代码审计工具链）

## 更新记录

- **2026-06-16**：初始化全景页，sqli-labs 25-30 总结归档
