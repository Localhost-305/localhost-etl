# FROM python:3.11-slim
# WORKDIR /app
# COPY /etl_project/requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
# COPY . .
# ENTRYPOINT ["python", "etl_project/main.py"]

FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r etl_project/requirements.txt
ENTRYPOINT ["python", "etl_project/main.py"]