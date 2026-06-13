# http头部注入

　　根据提示进行登录

![image](assets/image-20251115155706-d1ho6vx.png)

　　发现会回显我们的UA头和accept信息

　　我们退出登录，重新登录并且抓包

![image](assets/image-20251115160303-7uqb4kf.png)

　　尝试对UA头进行注入：

　　User-Agent: 1' or updatexml(1,concat(0x7e,(select database()),0x7e),1) or '

![image](assets/image-20251115160429-3r22xuh.png)

　　后续操作就和报错注入一样

　　‍
