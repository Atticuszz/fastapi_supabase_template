# 第一阶段：使用 Poetry 安装依赖
FROM python:3.11-rc-slim as builder

WORKDIR /app

RUN pip install poetry

COPY poetry.lock  pyproject.toml /app/
# TODO: login docker register plugin
# 安装依赖，忽略项目本身
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-root

# 第二阶段：构建最终镜像
FROM python:3.11-rc-slim

ENV PYTHONPATH=/app/src
WORKDIR /app

# 从 builder 阶段复制安装好的依赖
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# 复制整个项目到容器中
COPY . /app

# 设置环境变量
ENV PORT=5000


# 暴露端口
EXPOSE 5000

# 运行 FastAPI 应用
CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "5000"]
