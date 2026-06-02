---
title: Codex 入库规则
type: system
version: 2.0
domain: 信息安全 / 网络安全
---

# Codex 入库规则

研究领域：信息安全 / 网络安全
Vault 路径：D:\obsidian\security-notes

## 判断流程

1. **相关性**：是否与信息安全、网络安全、渗透测试、漏洞分析、靶场、工具链、应急响应、攻防研究相关。
2. **新鲜度**：是否包含新漏洞、新工具、新案例、新趋势、新版本变化。
3. **价值度**：是否值得保存、引用、复盘、实验或继续研究。
4. **可输出性**：是否能转化为文章、报告、视频脚本、课程、周报或研究笔记。
5. **关联性**：是否能连接到已有笔记、靶场记录、工具卡片、漏洞类型或研究专题。

## 分类标准

### 漏洞分类
- 按 **OWASP Top 10** 分类：注入、失效的认证、敏感数据暴露、XXE、失效的访问控制、安全配置错误、XSS、不安全的反序列化、使用含已知漏洞的组件、不足的日志和监控
- 按 **CWE** 编号索引：用于精确的技术分类
- 按 **CNVD/CVE** 编号：用于官方漏洞库关联

### 攻击技术分类
- 按 **MITRE ATT&CK** 矩阵映射：侦察、初始访问、执行、持久化、提权、防御规避、凭据访问、发现、横向移动、收集、命令控制、数据窃取、影响
- 按攻击面分类：Web应用、网络服务、终端、移动、云、IoT

### 靶场分类
- 按平台：DVWA、Pikachu、sqli-labs、upload-labs、Vulhub、HackTheBox、TryHackMe、CTFHub
- 按技术领域：Web安全、密码学、逆向、Pwn、杂项、内网渗透、权限提升

### 工具分类
- **信息收集**：Nmap、Masscan、Fscan、Nuclei、Shodan、FOFA
- **漏洞扫描**：Nessus、AWVS、AppScan、OpenVAS
- **漏洞利用**：Metasploit、Cobalt Strike、sqlmap、Burp Suite
- **后渗透**：Mimikatz、Empire、Covenant、Sliver
- **密码破解**：Hashcat、John the Ripper、Hydra、Medusa
- **流量分析**：Wireshark、tcpdump、Burp Suite
- **逆向分析**：IDA Pro、Ghidra、OllyDbg、x64dbg
- **综合工具**：Python脚本、PowerShell、Bash脚本

## 入库动作

- `S 进选题池`：有研究潜力，放入 `03_Topics/选题池`。
- `A 做知识卡片`：可以沉淀为可复用知识，放入 `02_Knowledge` 对应子目录：
  - 漏洞分析 → `02_Knowledge/漏洞卡片`
  - 攻击技术 → `02_Knowledge/攻击技术`
  - 防御方案 → `02_Knowledge/防御方案`
  - 安全规范 → `02_Knowledge/安全规范`
  - 工具使用 → `02_Knowledge/工具卡片`
- `B 存参考资料`：暂时保留原文或摘录，放入 `01_Sources` 对应子目录。
- `C 归档`：已有处理结果或仅作记录，放入合适的归档目录。
  - 靶场通关 → `04_Outputs/靶场报告`
  - CTF比赛 → `04_Outputs/CTF-Writeup`
  - 学习笔记 → `03_Topics/靶场项目`
- `D 忽略`：不相关、低价值、重复或无法验证的信息不入库。

## 命名建议

- 漏洞卡片：`CVE-YYYY-NNNNN - 漏洞名称.md` 或 `漏洞名称 - OWASP分类.md`
- 攻击技术：`ATT&CK - 技术名称.md` 或 `攻击类型 - 具体技术.md`
- 工具卡片：`工具 - 工具名称.md`
- 靶场记录：`靶场 - 平台名 - 靶场名.md`
- CTF Writeup：`CTF - 比赛名 - 题目名.md`
- 日期型资料：`YYYY-MM-DD 主题.md`
- 输出内容：`YYYY-MM-DD 标题.md`

## 笔记要求

每条入库笔记尽量包含：
- **来源**：原始链接、文档出处
- **摘要**：核心内容概述
- **关键点**：技术要点、漏洞原理、利用条件
- **可信度**：信息可靠性评估
- **可行动作**：后续实验、复现、研究计划
- **相关链接**：关联的笔记、参考文献
- **后续问题**：待解决的问题、进一步研究方向

## 模板对照

| 笔记类型 | 使用模板 |
|---------|---------|
| 漏洞分析 | `Vulnerability-漏洞分析.md` |
| 攻击技术 | `Attack-攻击技术.md` |
| 工具卡片 | `Tool-工具卡片.md` |
| 靶场通关 | `Lab-靶场通关.md` |
| CTF Writeup | `CTF-Writeup.md` |
| 知识卡片 | `Knowledge-知识卡片.md` |
| 选题 | `Topic-选题.md` |
| 复盘 | `Review-复盘.md` |
