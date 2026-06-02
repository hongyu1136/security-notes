# Less-26 过滤了注释和空格的注入
## 查看分析源码
```php
$id= preg_replace('/or/i',"", $id);       // 去掉 or
$id= preg_replace('/and/i',"", $id);      // 去掉 and
$id= preg_replace('/[\/\*]/',"", $id);    // 去掉 /*
$id= preg_replace('/[--]/',"", $id);      // 去掉 --
$id= preg_replace('/[#]/',"", $id);       // 去掉 #
$id= preg_replace('/[\s]/',"", $id);      // 去掉空格、Tab、换行...
$id= preg_replace('/[\/\\\$$/',"", $id);  // 去掉 / 和 \
```
## 过滤方法：

**or 用双写 oorr 或 ||**  
**and 用双写 aandnd 或 &&（GET 里 && 要 URL 编码成 %26%26）**  
**注释废了 → 末尾用 ||'1，让模板自带 ' 补上**  
**空格废了 → 用 () 包裹替代**