# 安顺学院 asu.edu.cn — 攻击面侦查

> 2026.06.26 subfinder 被动收集

## 暑期优先目标

| 子域名 | 系统 | 考什么 |
|------|------|------|
| jwxt.asu.edu.cn | 教务系统 | SQLi / XSS |
| authserver.asu.edu.cn | 统一认证 | JWT / SSO / 认证绕过 |
| ehall.asu.edu.cn | 一站式服务大厅 | 越权 / 逻辑漏洞 |
| oa.asu.edu.cn | OA 办公系统 | 越权 / 弱口令 |
| mail.asu.edu.cn | 邮件系统 | 弱口令 |

## 全部子域名 (41)

```
asuoa.asu.edu.cn
authserver.asu.edu.cn
bwc.asu.edu.cn
crjyb.asu.edu.cn
dataup.asu.edu.cn
datax.asu.edu.cn
dns1.asu.edu.cn
dzxxxy.asu.edu.cn
ehall.asu.edu.cn
gh.asu.edu.cn
gzc.asu.edu.cn
gztpyj.asu.edu.cn
jjc.asu.edu.cn
jsgzc.asu.edu.cn
jxwlkc.asu.edu.cn
jwxt.asu.edu.cn
jyxy.asu.edu.cn
kyc.asu.edu.cn
lib.asu.edu.cn
ltx.asu.edu.cn
mail.asu.edu.cn
mlzyjyb.asu.edu.cn
oa.asu.edu.cn
rsc.asu.edu.cn
sjx.asu.edu.cn
tyxy.asu.edu.cn
webht.asu.edu.cn
www.asu.edu.cn
www.ykt.asu.edu.cn
xb.asu.edu.cn
xczx.asu.edu.cn
xlw.asu.edu.cn
xwny.asu.edu.cn
xww.asu.edu.cn
yikt.asu.edu.cn
ykt.asu.edu.cn
ysx1.asu.edu.cn
yyyyx.asu.edu.cn
zdxk.asu.edu.cn
```


## httpx探测存活
```
http://authserver.asu.edu.cn
http://ehall.asu.edu.cn
https://ykt.asu.edu.cn
http://mail.asu.edu.cn
```

## 攻击面分析（6.26 人工踩点）

| 子域名 | 猜测功能 | 实测结果 |
|------|---------|---------|
| authserver | 统一认证 CAS | ✅ 登录页 |
| ehall | 一站式服务大厅 | ✅ 跳转 CAS |
| ykt | 一卡通系统 | ✅ 跳转 CAS（HTTPS） |
| mail | 邮件系统 | ⚠️ 未跳转 CAS，可能独立认证 |

### 🔴 关键发现

**authserver + ehall + ykt 共用同一 SSO。** 这意味着：

- CAS 是单点瓶颈 — 绕过 authserver 就穿全站（ehall + ykt 全通）
- ykt 含消费流水、余额、门禁数据，是最值钱的目标
- mail 可能独立认证或也存在 SSO 重定向，需进一步验证

暑假优先打 authserver：测试 JWT 伪造、登录绕过、弱口令、未授权接口。