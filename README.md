# oauth_server
基于 authlib 框架下的Oauth2.0认证服务.

## 认证流程
### password 认证模式

```
1. curl -u ${client_id}:${client_secret} -XPOST http://127.0.0.1:5000/oauth/token -F grant_type=password -F username=${username} -F password=valid -F scope=profile

2. curl -H "Authorization: Bearer ${access_token}" http://127.0.0.1:5000/api/me

```

### authorization_code 认证模式

```
1. 获取code
open http://127.0.0.1:5000/oauth/authorize?response_type=code&client_id=${client_id}&scope=profile

2. 使用code获取access token
curl -u ${client_id}:${client_secret} -XPOST http://127.0.0.1:5000/oauth/token -F grant_type=authorization_code -F scope=profile -F code=${code}
 
3. 使用tocken请求接口
curl -H "Authorization: Bearer ${access_token}" http://127.0.0.1:5000/api/me
```

## 启动说明
- 因为oauth2.0是通过https传输数据的,所以在没有https的情况下(开发环境),参考下面解决办法:
### windows
```
set FLASK_ENV=development
set AUTHLIB_INSECURE_TRANSPORT=1
flask run
```

### linux

```
import os
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = '1'


flask run
```
