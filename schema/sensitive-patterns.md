---
title: Sensitive Content Detection Rules
type: schema
public: true
created: 2026-06-16
updated: 2026-06-16
---

# 敏感内容检测规则

> 用于 pre-commit hook 和定期扫描，防止敏感信息泄露到公开仓库。

## 检测模式

### API 密钥 & Token

```regex
# AWS Access Key
AKIA[0-9A-Z]{16}

# GitHub Token
ghp_[0-9a-zA-Z]{36}
github_pat_[0-9a-zA-Z]{22,}

# Generic API Key patterns
(api_key|apikey|api_secret|secret_key|access_key)\s*[:=]\s*['"][^'"]+['"]

# JWT Token
eyJ[a-zA-Z0-9_-]{10,}\.[a-zA-Z0-9_-]{10,}\.[a-zA-Z0-9_-]{10,}
```

### 密码 & 凭据

```regex
# Password in config
(password|passwd|pwd)\s*[:=]\s*['"][^'"]+['"]

# Connection strings
(mysql|postgres|mongodb|redis)://[^@]+@[^/\s]+

# Private keys
-----BEGIN (RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----
```

### 个人信息 (PII)

```regex
# Chinese ID Card (18 digits)
[1-9]\d{5}(19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{3}[\dXx]

# Chinese Phone Number
1[3-9]\d{9}

# Email (internal/private domains only)
[\w.-]+@(internal\.example\.com|private\.corp)
```

### 内部信息

```regex
# Internal IP ranges
(10\.\d{1,3}|172\.(1[6-9]|2\d|3[01])|192\.168)\.\d{1,3}\.\d{1,3}

# Internal hostnames
[\w-]+\.(internal|corp|local|lan)

# Internal URLs
https?://[\w.-]+\.(internal|corp|local)
```

## Pre-commit Hook 检查项

1. **扫描暂存区 `wiki/` 和 `schema/` 文件**
   - 匹配上述正则模式
   - 检查 YAML frontmatter `public: false`
2. **检查 `raw/` 和 `_private/` 文件**
   - 确认不在暂存区（被 .gitignore 排除）
3. **检查大文件**
   - 拒绝 >10MB 的二进制文件
   - 警告 >1MB 的 PNG/JPEG 附件

## 误报处理

- 靶场/CTF 中的示例凭据：添加注释标记 `# nosec` 或 frontmatter `sensitive: false`
- 公开的测试密钥：确认来源是公开文档后放行

## 更新记录

- **2026-06-16**：初始版本，覆盖 API 密钥、密码、PII、内部信息四类
