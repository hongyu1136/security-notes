# 存储型xss

　　存储型与反射性的区别就是，反射型是一次性的，而存储型是存在数据库中的，每请求一次就会触发一次

　　留言列表不删除，每刷新一次就会触发一次 也就是切换页面回来也会有xss弹窗

　　payload：

　　<script>alert('xss')</script>

　　‍

![image](assets/image-20251111205022-cm8x2lp.png)
