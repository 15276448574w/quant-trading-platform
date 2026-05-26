# 🚀 快速开始指南

## 环境要求

- Python 3.9+
- Node.js 16+
- Docker & Docker Compose
- MySQL 8.0+（可选，Docker 提供）
- Redis 6.0+（可选，Docker 提供）

## 使用 Docker Compose 启动（推荐）

### 1. 克隆项目

```bash
git clone https://github.com/15276448574w/quant-trading-platform.git
cd quant-trading-platform
```

### 2. 复制环境配置

```bash
cp .env.example .env
```

### 3. 启动所有服务

```bash
docker-compose up -d
```

### 4. 查看日志

```bash
docker-compose logs -f
```

### 5. 访问应用

- 前端：http://localhost:3000
- 后端 API：http://localhost:8000
- API 文档：http://localhost:8000/docs
- Swagger UI：http://localhost:8000/swagger-ui

### 6. 停止服务

```bash
docker-compose down
```

---

## 本地开发（不使用 Docker）

### 后端配置

#### 1. 创建虚拟环境

```bash
cd backend
python -m venv venv

# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

#### 2. 安装依赖

```bash
pip install -r requirements.txt
```

#### 3. 配置数据库

```bash
cp .env.example .env
# 编辑 .env 文件，配置数据库连接
```

#### 4. 启动后端

```bash
python main.py
```

后端将运行在 http://localhost:8000

### 前端配置

#### 1. 安装依赖

```bash
cd frontend
npm install
```

#### 2. 配置环境

```bash
cp .env.example .env
# 编辑 .env 文件，配置 API 地址
```

#### 3. 启动前端

```bash
npm start
```

前端将运行在 http://localhost:3000

---

## 故障排除

### 问题：Docker 端口已被占用

**解决方案**：
```bash
# 修改 docker-compose.yml 中的端口映射
# 或停止占用该端口的其他服务
```

### 问题：数据库连接失败

**解决方案**：
```bash
# 检查 MySQL 服务是否运行
# 检查 .env 中的数据库配置是否正确
# 重启数据库
docker-compose restart mysql
```

### 问题：前端无法连接到后端 API

**解决方案**：
```bash
# 检查 .env 中的 REACT_APP_API_URL 是否正确
# 检查后端是否在运行
# 检查浏览器控制台是否有 CORS 错误
```

---

## 常用命令

```bash
# 查看所有运行的容器
docker-compose ps

# 查看特定服务日志
docker-compose logs backend
docker-compose logs frontend

# 进入容器命令行
docker-compose exec backend bash

# 重启特定服务
docker-compose restart backend

# 删除所有容器和数据
docker-compose down -v
```

---

## 下一步

- 查看 [API 文档](./API.md)
- 查看 [开发指南](./DEVELOPMENT.md)
- 查看 [架构设计](./ARCHITECTURE.md)
