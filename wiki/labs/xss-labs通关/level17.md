# Level 17 — embed 标签双参数拼事件

## 发现过程

URL 有两个参数 `arg01` `arg02`，都过了 `htmlspecialchars`。拼进 `<embed>` 标签时没加引号：

```php
echo "<embed src=xsf01.swf?".htmlspecialchars($_GET["arg01"])."=".htmlspecialchars($_GET["arg02"])."...>";
```

两个参数的值拼在一起，中间只有 `=` 隔开，可以控制整个属性区。

## Payload 尝试

`onmouseover` 不行——embed 指向的 swf 不存在，渲染出来零高度鼠标碰不到。

换 `onfocus` + `autofocus`：

```
?arg01=1 onfocus=alert(1) autofocus&arg02=
```

打开页面自动触发，不需要交互。

## 要点

- `htmlspecialchars` 只杀 `<>&"'`，不杀空格
- 属性没引号时，空格直接断开，后面随便写事件
- `onmouseover` 碰不到元素时换 `onfocus` + `autofocus`
