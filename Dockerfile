FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r etl_project/requirements.txt
# RUN mkdir -p shared/files/upload
# RUN chmod -R 755 shared/files/upload
ENTRYPOINT ["python", "etl_project/src/main.py"]