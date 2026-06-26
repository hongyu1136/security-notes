---
title: Claude Code 自动化机制
type: workflow
tags: [ClaudeCode, Agent, 自动化, Loop, Hook, 工作流]
public: true
created: 2026-06-16
updated: 2026-06-16
---

# Claude Code Agent 自动化机制

> Claude Code 四种自动化形态的原理、组合方式、实操案例。

## 四种自动化形态

| 形态 | 触发方式 | 适用场景 |
|------|---------|---------|
| `/loop` | 定时 cron | 周期性检查（监控、轮询、日报） |
| `/goal` | 目标驱动 | agent 持续运行直到达标或卡住 |
| `hooks` | 事件触发 | 编辑文件后跑 lint、结束前验证构建 |
| 子 agent | 主 agent 派生 | 并行拆分任务，各自独立 goal 验证 |

**组合使用**：`/loop` 每周五触发 → 主 agent 分析 PR → 生成多个子 agent → 各自 goal loop 验证。

## `/loop` 本质

```
cron 调度 + prompt 注入

1. 解析时间间隔 → cron 表达式
2. 创建定时任务，立即执行第一次
3. 调度器每秒检查 → 到期后 prompt 入消息队列 → 触发 agent
```

**关键认知**：`/loop` 没有内置 evaluator，所有智能（达标判断、异常处理、决策）全部来自 prompt。

## 实操案例：监控公众号更新

### 架构

```
/loop (30分钟)
  → 读 sync_state.json 判断状态
  → API 请求最新文章
  → 对比 known_articles 识别新增
  → 更新状态文件 + 输出结果
```

### 状态机设计

| 上一轮状态 | 本轮动作 |
|-----------|---------|
| `success` | 正常同步，对比文章 |
| `token_expired` | 先轻量检测 token，未恢复则跳过 |
| API 返回 200003 | 标记 `token_expired`，通知扫码，不重试 |

### 核心设计原则

1. **状态外部化**：`sync_state.json` 持久化状态，跨轮次传递上下文
2. **渐进式恢复**：token 失效后不反复重试，等用户操作后再恢复
3. **最小化 token 消耗**：无更新时仅输出"无更新"三个字
4. **异常分类处理**：凭证过期 vs 网络超时 → 不同策略

## Loop 设计方法论

1. **先写 skill，再加 loop** — loop 只是定时唤醒，核心能力在 prompt/skill
2. **状态文件是必需品** — 纯上下文记忆在跨轮次会丢失
3. **异常处理靠 prompt 智能判断** — agent 可处理 prompt 中未逐一列举的边界情况，这比传统 cron 脚本强一个维度
4. **每轮尽量轻量** — 先读状态、先做低成本检测，无变化直接退出
