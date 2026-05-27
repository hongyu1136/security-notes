# pass-10

　　查看源码

![image](assets/image-20251209190714-9wir7br.png)

　　这关与前几关不同 这里使用的是

　　**str_ireplace()函数这将我们的危险后缀都替换为空了**

　　同样 代码是死的 它仅执行一次 那么我们使用双写

　　**将一个php去掉后，然后拼接了一个新的php**

　　后缀为 **.pphphp**

　　bp抓包

![image](assets/image-20251209191106-s9kfuxh.png)

![image](assets/image-20251209191140-nqib84e.png)

　　连接成功
