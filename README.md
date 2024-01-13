<p align="center">
  <img src="assets/logo.png" alt="Logo">
</p>

<p align="center">
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
  </a>
  <a href="https://codecov.io/gh/Atticuszz/fastapi_supabase_template">
    <img src="https://codecov.io/gh/Atticuszz/fastapi_supabase_template/branch/main/graph/badge.svg?token=YOUR_TOKEN" alt="codecov">
  </a>
  <a href="https://github.com/Atticuszz/fastapi_supabase_template/actions">
    <img src="https://github.com/Atticuszz/fastapi_supabase_template/actions/workflows/ci.yml/badge.svg" alt="CI">
  </a>
  <a href="https://github.com/Atticuszz/fastapi_supabase_template/releases/">
    <img src="https://img.shields.io/github/release/Atticuszz/fastapi_supabase_template.svg" alt="GitHub release">
  </a>
  <img src="https://img.shields.io/badge/python-3.10|3.11|3.12-blue.svg" alt="Python">
  <a href="https://supabase.com">
    <img src="https://supabase.com/badge-made-with-supabase-dark.svg" alt="Made with Supabase">
  </a>
</p>

# ⚡SupaFast⚡
___
> supabase &  fastapi crud template
## Roadmap 🫶
___
- [x] FastAPI backend
  - [x] **standard** structure for <a href="https://github.com/tiangolo/fastapi" class="external-link" target="_blank">**FastAPI**</a> project 
  ```text
  ── src
  │   └── app
  │       ├── api
  │       │   ├── api_v1
  │       │   │   ├── endpoints
  │       │   │   │   ├── __init__.py
  │       │   │   │   └── items.py
  │       │   │   ├── __init__.py
  │       │   │   └── api.py
  │       │   ├── __init__.py
  │       │   └── deps.py
  │       ├── core
  │       │   ├── __init__.py
  │       │   ├── config.py
  │       │   └── events.py
  │       ├── crud
  │       │   ├── __init__.py
  │       │   ├── base.py
  │       │   └── crud_item.py
  │       ├── schemas
  │       │   ├── __init__.py
  │       │   ├── auth.py
  │       │   ├── base.py
  │       │   ├── item.py
  │       │   └── msg.py
  │       ├── services
  │       │   └── __init__.py
  │       ├── utils
  │       │   └── __init__.py
  │       ├── __init__.py
  │       └── main.py
  ...
  ```
  - [x] **auto-auth** by fastapi dependency with supabase-auth
  - [x] Full coverage of **CRUD** operations and **api** tests
  - [x] pytest integration
- [ ] Supabase integration
  - [x] crud supabase-postgresql
  - [ ] websocket with supabase-realtime 
  - [ ] curd supabase-storage
  - [ ] supafunc integration
- [ ] deployment
  - [ ] Full **Docker** integration (Docker based).


## How to use it
___
![](assets/usage.gif)
## Release Notes 🥸
___
### Latest Changes
### 2024-01-13 by Atticuszz - feat: update ci and README.md
- 🚚 [img.png](img.png) <- img.png
### 2024-01-13 by Atticuszz - upgrade: release 0.1.0
- 🔨 [items.py](src/app/api/api_v1/endpoints/items.py)
- 🔨 [deps.py](src/app/api/deps.py)
- 🔨 [config.py](src/app/core/config.py)
- 🔨 [base.py](src/app/crud/base.py)
- 🔨 [crud_item.py](src/app/crud/crud_item.py)
- 🔨 [__init__.py](src/app/schemas/__init__.py)
- 🔨 [auth.py](src/app/schemas/auth.py)
- 🔨 [base.py](src/app/schemas/base.py)
### 2024-01-12 by Atticuszz - bugs: failed to auth as dep on new user by access token
- 🔨 [items.py](src/app/api/api_v1/endpoints/items.py)
- 🔨 [deps.py](src/app/api/deps.py)
- 🔨 [events.py](src/app/core/events.py)
### 2024-01-12 by Atticuszz - fix: fix pytest bug of failed test gotrue client in trio, feat: add crud test
- 🔨 [items.py](src/app/api/api_v1/endpoints/items.py)
- 🔨 [deps.py](src/app/api/deps.py)
- 🔨 [config.py](src/app/core/config.py)
- 🔨 [base.py](src/app/crud/base.py)
- 🔨 [crud_item.py](src/app/crud/crud_item.py)
- 🔨 [auth.py](src/app/schemas/auth.py)
- 🔨 [base.py](src/app/schemas/base.py)
- 🔨 [item.py](src/app/schemas/item.py)
## License

This project is licensed under the terms of the MIT license.
