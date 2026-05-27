# pass-19

　　查看源码

![image](assets/image-20251213194430-f3111c0.png)

　　代码审计:

　　发现它并未对上传文件进行判断，仅是对保存文件名进行判断

　　并且也只是和黑名单进行了判断，并没有进行任何后缀过滤措施

　　利用windows特性，利用点 空格或是 **::$DATA** 进行绕过

![image](assets/image-20251213195045-ezu7ty4.png)

　　上传成功

　　连接成功

![image](assets/image-20251213195124-w8vto8e.png)
