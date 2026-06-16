---
title: AI Skills 方法论 — 用 AI 辅助安全研究
type: workflow
tags: [AI, Skills, 方法论, 安全工具, 提示工程]
public: true
created: 2026-06-16
updated: 2026-06-16
---

# AI Skills 方法论

> Skill 不是大脑，是操作规程。就像飞行员 checklist——checklist 不会开飞机，但能让飞行员不出低级错误。

## Skill 本质

一个 Skill = Markdown 文件 = 结构化 Prompt 模板，三段式结构：

```
---
name: skill-name
description: 触发条件
---
# 方法论（步骤化流程约束）
Phase 1 → Phase 2 → Phase 3
每阶段有 MUST 输出 checkpoint

# references/（知识库）
按需 Read 不预设，payload/案例/指纹库
```

## Skill 的三个作用

| 作用 | 说明 |
|------|------|
| ① 约束模型不确定性 | 强制线性流程，防跳步（先 scope → 再侦察 → 再探测） |
| ② 补充领域知识 | Claude 不知道通达 OA 默认密码、特定指纹特征 → reference 注入 |
| ③ 防幻觉 | 「不准凭记忆出 payload，必须 Read 对应 playbook」 |

## 漏洞发现的合力模型

```
方法论 (skill 提供)
    ↓ 指导
推理能力 (模型提供)
    ↓ 分析
领域经验 (reference 提供)
    ↓ 匹配
漏洞发现
```

Skill 提升的是**下限**，不是上限。好的 skill 让你不遗漏基础步骤，但发现漏洞的那一步靠的是模型推理 + 人的判断。

## AI 挖洞 vs 基础学习

| | 纯学习（5h×2天） | AI辅助（1h配置） |
|---|---|---|
| 找到的 | 1-2 个理解透的逻辑洞 | 20+ 个表面特征匹配 |
| 质量 | 能写出完整利用链 | 大量误报需验证 |
| 长期 | 下次更快 | 每次都从零开始 |

**正确用法**：用 AI 加速接触面，用基础做判断。AI 不会让你跳过基础，只会让你看到基础为什么重要。

## 总结

> Skill 是操作规程，Reference 是别人的经验，模型是推理引擎，你是决策者。四个缺一不可。
