# 字符型注入（get）

　　先尝试一下闭合类型

　　在url中name=后面输入

　　1' 报错

![image](assets/image-20251112211125-uc8jktx.png)

　　1'' 正常 说明是字符型注入

　　猜测闭合符为' 尝试构造万能密码：

　　 **' or '1'='1**

![image](assets/image-20251112211245-17m1k5j.png)

　　我们也可以查询所有的表，数据库

　　查所有表:

![image](assets/image-20251112211422-14ul46e.png)

　　后续就不演示了
