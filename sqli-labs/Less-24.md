# Less-24 二次注入
## 分析查看源码
**注册**（login_create.php）— username 被转义了，直接注不了：
```php
$username= mysql_escape_string($_POST['username']);
$sql = "insert into users (username, password) values(\"$username\", \"$pass\")";
```
**改密码**（pass_change.php）— 从 session 取的 username **没有转义**，注入点在这里：
```php
$username= $_SESSION["username"];  // 从数据库取出来，没过滤！
$sql = "UPDATE users SET PASSWORD='$pass' where username='$username' and password='$curr_pass' ";
```
## 过程

**注册用户（username带payload） → 存入数据库 → 登录 → 改密码 → SQL注入触发**

例：
注册使用admin'#
密码:123456
![](99_Attachments/图片/Less-24/file-20260602155631933.png)
