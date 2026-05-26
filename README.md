# 🚀 Quant Trading Platform - 量化交易平台

一个完整的开源量化投资交易系统，支持策略研发、回测分析、实盘交易、风险管理。

## ✨ 核心特性

- 📊 **数据获取** - 集成 Tushare、AKShare 等多数据源
- 🔄 **回测引擎** - 高效的策略回测框架
- 📈 **策略管理** - 灵活的策略编写与参数优化
- 💼 **账户管理** - 实时持仓、资产追踪
- 📱 **现代化UI** - React 前端，实时数据展示
- 🛡️ **风险管理** - 多维度风险监控与预警
- 🔌 **实盘对接** - 支持多家券商接口

## 🏗️ 项目架构

```
quant-trading-platform/
├── backend/                 # FastAPI 后端
│   ├── app/
│   │   ├── api/            # API 路由
│   │   ├── core/           # 核心业务逻辑
│   │   ├── data/           # 数据处理
│   │   ├── models/         # 数据模型
│   │   ├── schemas/        # Pydantic schemas
│   │   ├── db/             # 数据库配置
│   │   └── utils/          # 工具函数
│   ├── main.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
├── frontend/                # React 前端
│   ├── src/
│   │   ├── pages/          # 页面组件
│   │   ├── components/     # 通用组件
│   │   ├── services/       # API 服务
│   │   ├── store/          # Redux 状态管理
│   │   ├── styles/         # 样式文件
│   │   ├── App.tsx
│   │   └── index.tsx
│   ├── package.json
│   ├── Dockerfile
│   └── .env.example
├── docs/                    # 文档
│   ├── API.md              # API 文档
│   ├── SETUP.md            # 部署指南
│   └── DEVELOPMENT.md      # 开发指南
├── docker-compose.yml      # Docker Compose 配置
├── .github/
│   └── workflows/          # CI/CD 工作流
└── README.md
```

## 🛠️ 技术栈

| 层级 | 技术 |
|-----|------|
| **前端** | React 18 + TypeScript + Ant Design + ECharts |
| **后端** | Python 3.9+ + FastAPI + SQLAlchemy |
| **数据库** | MySQL + Redis |
| **数据处理** | Pandas + NumPy + Tushare + AKShare |
| **回测** | Backtrader / 自建引擎 |
| **容器化** | Docker + Docker Compose |
| **实时通信** | WebSocket |

## 📦 快速开始

### 前置要求
- Python 3.9+
- Node.js 16+
- Docker & Docker Compose
- MySQL 8.0+
- Redis 6.0+

### 本地开发

#### 1. 克隆项目
```bash
git clone https://github.com/15276448574w/quant-trading-platform.git
cd quant-trading-platform
```

#### 2. 启动服务
```bash
# 使用 Docker Compose（推荐）
docker-compose up -d

# 或手动启动

# 后端
cd backend
python -m pip install -r requirements.txt
python main.py

# 前端（新终端）
cd frontend
npm install
npm start
```

#### 3. 访问应用
- 前端: http://localhost:3000
- API: http://localhost:8000
- API 文档: http://localhost:8000/docs

## 📚 文档

- [快速开始指南](./SETUP.md)
- [开发指南](./DEVELOPMENT.md)
- [API 文档](./API.md)
- [架构设计](./ARCHITECTURE.md)

## 📋 功能清单

### MVP (第一阶段)
- [x] 项目结构搭建
- [ ] 数据获取与缓存
- [ ] 回测引擎核心
- [ ] 策略管理基础
- [ ] Dashboard 界面
- [ ] 回测分析展示

### Phase 2 (第二阶段)
- [ ] 实时行情推送
- [ ] 持仓管理功能
- [ ] K线图表展示
- [ ] 交易记录查询

### Phase 3 (第三阶段)
- [ ] 实盘交易对接
- [ ] 风险管理模块
- [ ] 因子分析工具
- [ ] 策略对比分析

## 🔄 工作流

```
数据获取 → 数据缓存 → 策略计算 → 信号生成 → 回测/实盘 → 结果分析
```

## 📞 支持

- 📖 [GitHub Discussions](https://github.com/15276448574w/quant-trading-platform/discussions)
- 🐛 [提交 Issue](https://github.com/15276448574w/quant-trading-platform/issues)

## 📄 许可证

MIT License - 详见 [LICENSE](./LICENSE) 文件

---

**开发者**: 15276448574w  
**最后更新**: 2026-05-26  
**版本**: 0.1.0 (MVP)
