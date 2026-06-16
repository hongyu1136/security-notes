---
title: Operation Log
type: log
public: true
created: 2026-06-16
updated: 2026-06-16
---

# 操作日志

> 追加型日志。每次 Wiki 操作（摄入、重构、校验）在此记录。
> 格式：`YYYY-MM-DD HH:MM — 类型 — 摘要`

## 2026-06-16

- **19:17** — `refactor` — LLM Wiki 三层架构重构：迁移全部笔记到 raw/wiki/schema 结构
  - 源 → 目标：500+ 文件通过 `git mv` 迁移
  - 创建 `schema/CLAUDE.md` Wiki 操作规范
  - 创建 `wiki/index.md` 全局索引
  - 创建 `wiki/overview.md` 领域全景
  - 创建 `wiki/log.md` 操作日志
  - 更新 `README.md` 反映新架构
  - 更新 `.gitignore`：giignore raw/ 目录
  - 创建 `.githooks/pre-commit` 隐私检查钩子

## 2026-06-02

- **14:56** — `init` — 初始化知识库结构
  - 创建 00_Inbox ~ 99_Attachments 目录体系
  - 添加 9 个笔记模板
  - 编写 Codex 入库规则
  - 初始化 .gitignore

## 2026-05-29

- sqli-labs Less-1 至 Less-24 通关完毕
