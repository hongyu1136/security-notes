# pass-8

　　查看分析源码

　　这关的过滤相较于上一关又**少了一个过滤(::$DATA)** 的字符串

　　**在windows环境下，不光会自动去除文件末尾的点和空格，同时(::$DATA)这个字符串，windows也会认为是非法字符，默认去除掉**

　　抓包

![image](assets/image-20251208195358-15sszsa.png)

　　连接是需要把地址中::$DATA删除

![image](assets/image-20251208210534-1b4zxam.png)
