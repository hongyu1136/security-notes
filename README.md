# security-notes 知识库

这是一个面向信息安全/网络安全学习与研究的 Obsidian Vault。

## 使用入口

- `00_Inbox/`：临时收集、自动抓取、手动剪藏，先放这里再处理。
- `01_Sources/`：原始资料，包括新闻、文章、论文、社媒、会议纪要和旧资料导入。
- `02_Knowledge/`：沉淀后的知识卡片，按漏洞、攻击技术、防御方案、安全规范、工具分类。
- `03_Topics/`：选题、问题清单、研究专题和长期项目。
- `04_Outputs/`：CTF Writeup、靶场报告、文章、报告、视频脚本、课程资料、周报总结等输出成果。
- `05_Review/`：每日简报、每周复盘、月度总结、知识库优化记录。
- `06_Skills/`：可复用的信息收集、漏洞挖掘、渗透测试、应急响应、报告撰写流程。
- `99_Attachments/`：图片、PDF、表格、视频素材、脚本、Payload 等附件。

## 快速参考

- **入库规则**：[[/_system/Codex-入库规则|Codex 入库规则]]
- **知识库地图**：[[/知识库地图|知识库地图]]
- **漏洞分析模板**：[[_templates/Vulnerability-漏洞分析|Vulnerability-漏洞分析]]
- **攻击技术模板**：[[_templates/Attack-攻击技术|Attack-攻击技术]]
- **工具卡片模板**：[[_templates/Tool-工具卡片|Tool-工具卡片]]
- **靶场通关模板**：[[_templates/Lab-靶场通关|Lab-靶场通关]]
- **CTF Writeup 模板**：[[_templates/CTF-Writeup|CTF-Writeup]]

## Codex 工作方式

当我让 Codex 处理新资料时，先看 `_system/Codex-入库规则.md`，再按以下流程处理：

1. **判断相关性**：是否与信息安全/网络安全相关
2. **选择模板**：根据内容类型选择合适的模板
3. **分类入库**：按 OWASP Top 10、MITRE ATT&CK、CWE 等标准分类
4. **建立关联**：添加标签、链接到相关笔记

## 已有靶场笔记

现有靶场笔记暂时保留在原目录，后续可以逐步整理为：
- `02_Knowledge/漏洞卡片` - 漏洞分析和复现记录
- `02_Knowledge/攻击技术` - 攻击手法和技术分析
- `02_Knowledge/工具卡片` - 工具使用记录
- `03_Topics/靶场项目` - 靶场实验和环境搭建
- `04_Outputs/靶场报告` - 靶场通关记录

## 安全领域分类

### 漏洞分类
- **OWASP Top 10 (2021)**：A01-A10 十大 Web 应用安全风险
- **CWE**：通用缺陷枚举，精确技术分类
- **CVE/CNVD**：官方漏洞库编号

### 攻击技术
- **MITRE ATT&CK**：14 个攻击阶段，200+ 技术点
- **攻击面**：Web 应用、网络服务、终端、移动、云、IoT

### 工具分类
- **信息收集**：Nmap、Masscan、Fscan、Nuclei、Shodan、FOFA
- **漏洞扫描**：Nessus、AWVS、AppScan、OpenVAS
- **漏洞利用**：Metasploit、Cobalt Strike、sqlmap、Burp Suite
- **后渗透**：Mimikatz、Empire、Covenant、Sliver
- **密码破解**：Hashcat、John the Ripper、Hydra、Medusa
- **流量分析**：Wireshark、tcpdump、Burp Suite
- **逆向分析**：IDA Pro、Ghidra、OllyDbg、x64dbg
- **综合工具**：Python 脚本、PowerShell、Bash 脚本

## 维护日志

- **2026-06-02**：初始化知识库结构，添加安全领域模板和分类体系
