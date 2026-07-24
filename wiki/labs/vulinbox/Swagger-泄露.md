# Swagger 泄露 — Vulinbox 四关

## 第一关：OpenAPI 2.0 JSON

接口文档直接返回，含所有路径、参数、请求体结构。

## 第二关：OpenAPI 3.0 JSON

新版格式，连生产/测试服务器 URL 都标了（`servers` 字段）。

## 第三关：Swagger UI 空白页面

页面加载 Demo 数据——但 `swagger-ui.html` 可访问本身就是信息泄露。攻击者可改 JS 的 `url` 参数指向内网，或据此推断服务器装了 Swagger。

## 第四关：Git 泄漏

```
/.git/HEAD → ref: refs/heads/master
→ GitHack 还原整站源码
→ flag.txt / 123.txt 到手
```

## 实战路径

```
swagger-ui.html → swagger.json → 全部接口 → 找到越权/RCE 入口
.git/HEAD      → GitHack     → 源码审计  → 白盒挖洞
```

## 常见 Swagger 路径字典

`/swagger/v1/swagger.json`  `/swagger-ui.html`  `/api-docs`  `/v2/api-docs`  `/v3/api-docs`  `/openapi.json`  `/doc.html`（Knife4j）

## 工具

- **Swagger JSON**：浏览器直接打开或用 curl/jq 格式化
- **.git 还原**：GitHack、git-dumper
