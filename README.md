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
> supabase & fastapi crud template

![supafast.drawio.png](assets%2Fsupafast.drawio.png)

## Features 🚀

___

### FastAPI&supabase

1. works of authorization all handled by supabase-py and fastapi **dependency** without any extra code
2. supabase-py crud integration with **pydantic** model validation

### Pytest

1. pytest integration with **pytest-cov**
2. pytest **fixtures** for fastapi client and supabase client
3. pytest **fixtures** for access_token and refresh_token
4. test for **CRUD** operations
5. test for **api** operations

### CI/CD

1. **codecov** for coverage report
2. **poetry** for dependency management and pytest integration
3. **pre-commit** for code quality
4. **latest_changes.yml** for auto update README.md
5. **Semantic Release** for auto release and changelog
6. **docker** for deployment

## How to use it

___
![](assets/usage.gif)

1. create your github repo and clone your repo

2. cd your repo and install dependencies

```shell
poetry install
```
3. set your supabase env

```shell
export SUPABASE_URL=your_supabase_url
export SUPABASE_KEY=your_supabase_key
```
4. config fastapi settings
```python
# src/app/core/config.py
class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SUPABASE_URL: str = Field(default_factory=lambda: os.getenv("SUPABASE_URL"))
    SUPABASE_KEY: str = Field(default_factory=lambda: os.getenv("SUPABASE_KEY"))
    SUPERUSER_EMAIL: str = Field(default_factory=lambda: os.getenv("SUPERUSER_EMAIL"))
    SUPERUSER_PASSWORD: str = Field(default=lambda: os.getenv("SUPERUSER_PASSWORD"))
    # SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl = "https://localhost"
    SERVER_PORT: int = 8000
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = []
    PROJECT_NAME: str = "fastapi supabase template"
    Config: ClassVar[ConfigDict] = ConfigDict(arbitrary_types_allowed=True)
```
5. run server
```shell
poetry run uvicorn src.app.main:app --reload
```

## Roadmap 🫶
___

- [x] FastAPI backend
    - [x] **standard** structure
      for <a href="https://github.com/tiangolo/fastapi" class="external-link" target="_blank">**FastAPI**</a> project
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
    - [x] **CRUD** operations pytest
    - [x] **api** requests pytest
- [ ] Supabase integration
    - [x] crud supabase-postgresql
    - [ ] websocket with supabase-realtime
    - [ ] curd supabase-storage
    - [ ] supafunc integration
- [x] deployment
    - [x] Full **Docker** integration (Docker based).
- [ ] clone
    - [ ] cookiecutter
## Release Notes 🥸

___

### Latest Changes
### 2024-01-15 by Atticuszz - fix: no need to pass refresh token for validation ,only access_token chore: bump supabase_py_async to 2.5.0
- 🔨 [items.py](src/app/api/api_v1/endpoints/items.py)
- 🔨 [deps.py](src/app/api/deps.py)
- 🔨 [__init__.py](src/app/core/__init__.py)
- 🔨 [events.py](src/app/core/events.py)
- 🔨 [base.py](src/app/crud/base.py)
- 🔨 [crud_item.py](src/app/crud/crud_item.py)
- 🔨 [main.py](src/app/main.py)
- 🔨 [auth.py](src/app/schemas/auth.py)
### 2024-01-13 by Atticuszz - feat: update ci and README.md
- 🚚 [img.png](img.png) <- img.png
## License

This project is licensed under the terms of the MIT license.
