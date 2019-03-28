## Aboout

### 简介

使用Flask 作为server 框架搭建的一个微服务后台，提供图片人脸检测服务。

是front-web 的后端项目。

### 项目依赖

已经freeze 到 env.txt 下

### 开发&测试环境:

- win10 
- python 3.6.x

## How to use ?

### 环境依赖

推荐使用python 虚拟环境进行包安装

```powershell
> cd \2019SandaU\code\backend
> virtualenv venv 
```

### 环境激活

```powershell
> venv\Scripts\activate.bat  
```

### 运行

```powershell
D:\2019SandaU\code\backend (master -> origin)
(venv) λ python app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

### 测试

这里使用[HttPie](https://httpie.org/) 进行接口测试

```powershell
> http http://127.0.0.1:5000/api-test
HTTP/1.0 200 OK
Content-Length: 56
Content-Type: application/json
Date: Thu, 28 Mar 2019 07:33:16 GMT
Server: Werkzeug/0.15.1 Python/3.6.8

{
    "result": "The backend is starting and just enjoying!"
}
```

