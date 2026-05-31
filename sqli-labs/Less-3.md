# Less3—— ')闭合

　　**输入?id=1' 看到页面报错信息，推断sql语句是单引号字符型且有括号，所以我们需要闭合单引号也要考虑括号**

![image](assets/image-20251108092538-hti2lrl.png)

　　 **?id=1'--+ 报错 说明是数字型注入** 

![image](assets/image-20251108093120-x9v0jmw.png)

　　 **?id=1')--+ 正常**

![image](assets/image-20251108092912-c6d002i.png)

　　**后续操作与第二关一致**
