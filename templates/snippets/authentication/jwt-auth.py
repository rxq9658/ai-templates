---
type: snippet
category: authentication
language: python
tags: [auth, jwt, security]
created: 2026-03-11
description: JWT认证实现代码
dependencies: [pyjwt]
source: templates/snippets/authentication/jwt-auth.py
github_url: https://github.com/risckee/ai-templates/blob/main/templates/snippets/authentication/jwt-auth.py
---

# JWT认证代码片段

## 描述

JWT（JSON Web Token）认证的实现代码，包含token生成、验证和刷新机制。

## 依赖

```bash
pip install pyjwt python-dateutil
```

## 代码

```python
import jwt
from datetime import datetime, timedelta
from typing import Dict, Optional

class JWTAuth:
    """JWT认证管理器"""

    def __init__(self, secret_key: str, algorithm: str = "HS256"):
        self.secret_key = secret_key
        self.algorithm = algorithm

    def generate_token(self, user_id: str, expires_hours: int = 24) -> str:
        """
        生成JWT token

        Args:
            user_id: 用户ID
            expires_hours: 过期时间（小时）

        Returns:
            JWT token字符串
        """
        payload = {
            'user_id': user_id,
            'exp': datetime.utcnow() + timedelta(hours=expires_hours),
            'iat': datetime.utcnow()
        }
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)

    def verify_token(self, token: str) -> Optional[Dict]:
        """
        验证JWT token

        Args:
            token: JWT token字符串

        Returns:
            解码后的payload，验证失败返回None
        """
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None

    def refresh_token(self, user_id: str) -> str:
        """
        刷新token（生成新token）

        Args:
            user_id: 用户ID

        Returns:
            新的JWT token
        """
        return self.generate_token(user_id, expires_hours=24)

# 使用示例
if __name__ == "__main__":
    auth = JWTAuth(secret_key="your-secret-key-here")

    # 生成token
    token = auth.generate_token(user_id="user123")
    print(f"Generated token: {token}")

    # 验证token
    payload = auth.verify_token(token)
    if payload:
        print(f"Token verified: {payload}")
    else:
        print("Token verification failed")
```

## 使用说明

1. 安装依赖：`pip install pyjwt python-dateutil`
2. 配置secret_key（建议使用环境变量）
3. 调用`generate_token()`生成token
4. 调用`verify_token()`验证token

## 安全建议

- 使用强密钥（至少32字符）
- 设置合理的过期时间
- 使用HTTPS传输token
- 不在token中存储敏感信息

## 相关

- [[OAuth2]]
- [[Session认证]]
