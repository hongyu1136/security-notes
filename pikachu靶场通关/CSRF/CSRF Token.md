# CSRF Token

　　在暴力破解模块做过关于token的

　　简单来说，后台会对我们在url中提交的token和服务器中生成的token进行比较，这里我们就无法通过伪造url进行修改个人信息了

![image](assets/image-20251112202826-xtqdz02.png)

　　使用burp抓包即可

![image](assets/image-20251112203516-gd5bwe3.png)
