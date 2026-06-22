# Level 13 — Cookie 注入

## 发现过程

打开页面没反应。看响应头有 `Set-Cookie: user=call+me+maybe%3F`，再看源码 `t_cook` 参数对应 `$_COOKIE['user']`。

![](99_Attachments/图片/level13/file-20260622195647961.png)
## Payload

Burp 截请求，加一行：

```
Cookie: user=" onclick="alert(1)" type="text"
```
![](99_Attachments/图片/level13/file-20260622195716623.png)
## 要点

- 后端先给你种 Cookie，再读 Cookie 拼 HTML
- 和 Referer/UA 同套路，只是数据源换成了 Cookie
- Headers 三连：Referer → User-Agent → Cookie，注入思路一模一样
