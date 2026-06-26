# ARL 灯塔 — 资产侦查平台

## 是什么

ARL = Asset Reconnaissance Lighthouse，开源资产侦查系统。把你手动跑的 subfinder + httpx + nuclei 打包成一个 Web 界面，自动调度。

## 核心功能

| 功能 | 对应手动命令 | 说明 |
|------|------------|------|
| 子域名收集 | subfinder | 定时跑，自动更新 |
| 存活检测 | httpx | 自动筛 |
| 指纹识别 | 人工猜 | 识别 CMS/框架/中间件 |
| 文件泄露 | 手动跑字典 | 自动扫 .git/备份文件等 |
| 漏洞探测 | nuclei | 可关联批量扫 |

## 部署

在 Kali 上用 Docker：

```bash
cd /opt
git clone https://github.com/TophantTechnology/ARL
cd ARL/docker
docker compose up -d
```

浏览器 `http://<kali_ip>:5003`，初始密码 `arlpass`。

## 什么时候用

- 管理 3 个以上目标时
- 需要持续监控资产变化时
- 手动跑命令已经觉得烦的时候

**不是必须的**。你目前的 8 校侦查用手动能搞定，先把手动工具链练熟。

## 硬件要求

| 组件 | 最少 | 建议 |
|------|------|------|
| 内存 | 8GB | 16GB |
| 磁盘 | 50GB | 100GB+（MongoDB 吃盘） |

我的 Kali VM 8GB 刚好够，笔记本 Windows 搭不了（没有 Hyper-V/WSL2）。

## 和手动工具链对比

| | 手动链 | ARL |
|------|--------|-----|
| 上手成本 | 低 | 中（Docker + Web界面） |
| 灵活度 | 高 | 中 |
| 批量效率 | 低 | 高 |
| 持续监控 | 需要自己写定时 | 自带 |
| 指纹识别 | 人工 | 自动（准度一般） |
