# Less-22 基于错误的双引号字符型Cookie注入
## 分析查看源码
```php
// Less-22
$cookee1 = '"'. $cookee. '"';
$sql="SELECT * FROM users WHERE username=$cookee1 LIMIT 0,1";     // 闭合 "
```
与上关一样，只是闭合从 ') 变为"
不展示
