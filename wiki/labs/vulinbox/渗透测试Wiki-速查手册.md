# Vulinbox 渗透测试 Wiki

> 来源：https://www.yaklang.com/Yaklab/wiki/  
> 整理：2026.07.14  
> 用途：实战检查清单

---

## 一、用户密码枚举

### 1.1 用户名密码枚举

登录框无次数限制、无验证码 → 直接爆破。

流程：抓登录包 → Yakit/Burp WebFuzzer → 加载字典 → 跑。

### 1.2 验证码可绕过（3种）

| 方法 | 操作 |
|------|------|
| 分步验证 | 先弹窗验证码 → 服务器返回 true → 后续包不带验证码。直接重放第二步的包 |
| 验证码置空 | 删除 `captcha` 参数或值为空发请求 |
| 前端校验 | 验证码只在前端 JS 判断 → Burp 直接发包绕过 |

### 1.3 验证码复用

同一验证码多次请求不刷新。抓一个正确验证码 → WebFuzzer 循环发 → 验证码不变。

### 1.4 验证码可识别

OCR 识别弱验证码（无噪点、无扭曲、4位纯数字）。Yakit 内置 OCR 功能可使用。

### 1.5 账号密码加密参数

| 情况 | 做法 |
|------|------|
| 密码 MD5 | WebFuzzer 标签 `md5(payload)` |
| Basic 认证 | `base64(user:pass)` 标签 |
| AES/RSA | 逆向前端 JS 找加密逻辑 |

### 1.6 通用框架默认密码

```
tomcat/tomcat · admin/admin123 · admin/123456
weblogic/weblogic1 · jboss/admin · root/root
```

---

## 二、任意用户登录

### 2.1 客户端验证绕过

服务器返回 flag 决定登录成败 → 抓响应包 → 改 `success:0` 为 `success:1`。

**案例**：用友 NC 控制台 → 任意密码 → 改返回包 `0→1` → 登录 administrator。

### 2.2 万能验证码

验证码固定值（0000、1234、8888），或服务端写死某个值永不变化。

### 2.3 验证码可爆破

验证码无次数限制 → 跑 0000-9999。

### 2.4 通用框架登录

已知漏洞框架：Shiro（默认KEY）、Fastjson（反序列化）、用友 NC（响应绕过）、通达 OA。

### 2.5 验证码未做绑定

同一个验证码可登录任意账号。抓验证码 → 换 username 参数 → 任意登录。

### 2.6 验证码回显

响应包里明文返回验证码。`{"code":"4729"}` → 直接填。

### 2.7 任意用户注册

注册接口无邀请码/管理员审批 → 直接注册 admin 权限账号。

### 2.8 任意用户密码重置

密码重置接口可枚举 → 改 user_id 参数 → 重置别人密码。

---

## 三、会话管理

| 测试项 | 做法 |
|--------|------|
| 会话固定 | 登录前后 Session ID 是否改变 |
| 注销有效性 | 退出后用旧 Session 是否还能访问 |
| 超时有效性 | 挂 30 分钟后 Session 是否失效 |
| 重定向携带 | 跳转到外部域时 Session 是否在 Referer 中泄露 |
| 会话伪造 | Session ID 是否可预测（递增/时间戳/简单编码） |

---

## 四、未授权访问 — 32 种框架速查

| 框架/服务 | 未授权路径 |
|-----------|-----------|
| ActiveMQ | `/admin/` · `/api/` |
| CouchDB | `/_utils/` · `/_all_dbs` |
| Docker | `v=1.39 version` · `/containers/json` |
| Nacos | `/nacos/v1/auth/users?pageNo=1&pageSize=9` |
| Dubbo | `/` Telnet 端口 |
| Druid | `/druid/index.html` |
| Elasticsearch | `/_nodes` · `/_cat/indices` · `/_plugin/head/` |
| Hadoop | `/node` · `/cluster` |
| Jenkins | `/manage/` · `/script/` → `println "whoami".execute().text` |
| Jupyter | `/terminals/` |
| Kibana | `/app/kibana` |
| K8s | `api/v1/pods` |
| MongoDB | 27017 端口无密码 |
| Memcached | 11211 端口 `stats` |
| Redis | 6379 端口 `CONFIG SET dir` · 写 SSH 公钥 |
| RabbitMQ | `/api/connections` |
| Solr | `/solr/admin/` |
| Spring Boot | `/actuator/env` · `/actuator/heapdump` |
| VNC | 5900 端口无密码 |
| WebLogic | `/console/` |
| ZooKeeper | 2181 端口 `dump` |
| Zabbix | `/zabbix.php?action=problem.view` |

---

## 五、常见漏洞类型

| 类型 | 利用 |
|------|------|
| 未授权访问 | 直接访问后台路径 / API 接口 → 无鉴权 |
| URL 重定向 | `?redirect=http://evil.com` |
| XSS | 反射/存储/DOM/Header 注入 |
| 任意文件下载 | `?file=../../../../etc/passwd` 或 `?path=C:\Windows\win.ini` |
| SSRF | `?url=http://127.0.0.1:8080` |
| 文件包含 | `?page=../../etc/passwd` |
| 信息泄露 | `.git/`、`.svn/`、`.DS_Store`、phpinfo、源码泄露 |
| 金额/数量篡改 | 抓包 → 改价格/数量 → 0元下单 |
| 逻辑越权 | 改 user_id / order_id → 查看/操作别人数据 |

---

## 六、Yakit 漏洞检测插件（28框架）

```
Axis2 · JBoss · WebLogic · Nginx · ThinkPHP · Apache · Jenkins
Struts2 · Elasticsearch · Laravel · Jetty · ThinkCMF · Dedecms
WordPress · PHPCMS · 华天动力OA · 一米OA · Confluence · Drupal
Ecshop · Discuz · MetInfo · Log4j · Goahead · Joomla · Spring
```

使用方式：Yakit → 漏洞检测 → 加载对应插件 → 填入目标 → 一键扫描。

---

## 七、实战检查清单

信息收集完成后，按此顺序逐一验证：

1. **端口扫描** → 对照第四节未授权服务列表
2. **登录框** → 对照第一、二节（枚举/验证码/默认口令/加密/客户端绕过）
3. **URL 参数** → 测 XSS/SQLi/SSRF/文件包含/重定向
4. **API 接口** → 测未授权/越权/任意下载
5. **敏感路径** → `.git/`、`actuator/`、`druid/`
6. **JS 审计** → 找隐藏接口/路径/加密逻辑
7. **Yakit 插件** → 框架识别后一键跑
