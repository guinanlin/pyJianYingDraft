# pyJianYingDraft FastAPI 升级方案

## 背景说明

### 当前现状
pyJianYingDraft 目前是一个纯 Python 库项目，主要提供剪映草稿文件的生成和管理功能。用户需要通过直接调用 Python 代码的方式来使用其功能，这种使用方式限制了项目的应用场景和扩展性。

### 升级目标
将项目升级为基于 FastAPI 的 Web 服务，主要目的是：
1. 提供标准的 RESTful API 接口，支持远程调用
2. 支持多用户并发访问
3. 便于与其他系统集成
4. 提供更好的可扩展性和维护性

### 升级收益
1. **解耦合**: 将核心逻辑与接口层分离，便于维护和升级
2. **易集成**: 提供标准的 HTTP 接口，方便其他系统集成
3. **多语言支持**: 客户端可以使用任何支持 HTTP 的编程语言
4. **并发处理**: 支持多用户同时访问和处理
5. **监控管理**: 便于添加日志、监控和告警功能

## 1. 项目结构调整

### 1.1 当前项目结构
```
pyJianYingDraft/
├── pyJianYingDraft/          # 核心库
├── docs/                     # 文档目录
├── readme_assets/           # 调试用的素材文件（可以移动）
├── test.py                  # 调试代码（可以移动）
├── test2.py                 # 调试代码（可以移动）
└── README.md
```

### 1.2 升级后的项目结构
```
pyJianYingDraft/
├── src/
│   ├── core/
│   │   └── pyJianYingDraft/     # 移动自原来的核心库目录
│   ├── api/                      # FastAPI 应用目录
│   │   ├── __init__.py
│   │   ├── main.py              # FastAPI 主程序
│   │   ├── routers/             # 路由模块
│   │   ├── services/            # 业务逻辑层
│   │   └── schemas/             # 数据模型
│   └── config/                   # 配置文件
├── tests/                        # 测试目录
│   ├── assets/                  # 测试用素材（移动自 readme_assets）
│   ├── integration/            # 集成测试
│   └── unit/                   # 单元测试
├── docs/                        # 文档目录（保持不变）
├── examples/                    # 示例代码目录
│   ├── basic_usage.py          # 移动自 test.py
│   └── advanced_usage.py       # 移动自 test2.py
├── requirements.txt             # 项目依赖
└── README.md                    # 项目说明
```

### 1.3 目录调整说明
1. **核心库迁移**
   - 将 `pyJianYingDraft/` 核心库移动到 `src/core/` 目录下
   - 保持核心库的内部结构不变

2. **测试资源整理**
   - 将 `readme_assets/` 移动到 `tests/assets/`
   - 整理为标准的测试资源目录

3. **示例代码迁移**
   - 将 `test.py` 和 `test2.py` 移动到 `examples/` 目录
   - 重命名为更具描述性的名称
   - 添加详细的注释说明

[... 其他内容保持不变 ...]
