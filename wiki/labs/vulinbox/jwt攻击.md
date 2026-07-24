# JWT 攻击 — Vulinbox 三关

## JWT 三段结构

```
Header.Payload.Signature
```

| 段 | 内容 | 示例 |
|------|------|------|
| Header | 算法、类型 | `{"alg":"HS256","typ":"JWT"}` |
| Payload | 数据 | `{"username":"admin"}` |
| Signature | HMAC 签名 | 用密钥 + Header.Payload 算出来的 |

---

## 第一关：Safe JWT（对照）

正常流程。alg=HS256，服务端用真密钥验签，改不了。

---

## 第二关：alg=none

```go
switch token.Header["alg"] {
case "none", "None":
    return jwt.UnsafeAllowNoneSignatureType, nil  // 跳过验签
}
```

**攻击**：Header 改 `alg:none` → 删签名 → 任意伪造身份。

Payload 示例：
- Header: `{"alg":"none","flag":true,"username":"admin"}`
- Payload: `{"username":"admin"}`
- 签名: 空

jwt.io 上切 Encoder，alg 选 none，右边生成 token 末尾只有一个点。

![](99_Attachments/图片/jwt攻击/file-20260626144309448.png)
---

## 第三关：错误泄露密钥

```go
if err != nil {
    return nil, fmt.Errorf("parse jwt faild, jwt: %v, key: %v,error: %v", authToken, key, err)
    //                                                              ^^^^^^^^^^^^ 密钥明文
}
```

**攻击**：发畸形 token 触发解析错误 → 响应里搜 `key:` → 拿到真密钥。

**密钥是 Go byte 数组**：`[88 82 111...]` → ASCII 转换工具还原成字符串。

拿到密钥后用 HS256 + 真密钥签名任意 token。

### 踩坑：flag 放哪

- `flag` 放 **Payload** → 没用。服务器从数据库查用户数据，payload 只做身份校验
- `flag` 放 **Header** → 生效。jwt-go 库会把 header 的自定义字段合并到解析后的 Map，被接口响应反射

```
Header: {"alg":"HS256","typ":"JWT","flag":1}  ← 这里
Payload: {"username":"admin"}
→ 服务器返回 {"flag":1, ...}
→ 前端 if(data.flag) → Win!
```

![](99_Attachments/图片/jwt攻击/file-20260626144334785.png)

---

## 两个核心攻击面的区别

| | alg=none | 密钥泄露 |
|------|------|------|
| 前提 | 服务端接受 alg:none | 服务端报错含密钥 |
| 难点 | 无 | Go []byte 转字符串 |
| 实战频率 | 老系统常见 | 少见但一打就穿 |

## 实战怎么用

登录口拿到 JWT → jwt.io 解码看结构 → 先试 alg:none → 不行看报错有没有泄露 key。
