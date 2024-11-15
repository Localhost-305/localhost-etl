# FROM python:3.11-slim
# WORKDIR /app
# COPY . .
# RUN pip install --no-cache-dir -r etl_project/requirements.txt
# RUN mkdir -p shared/files/upload && chmod -R 777 shared/files/upload
# ENTRYPOINT ["python", "-u", "etl_project/src/main.py"]

FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r etl_project/requirements.txt
ENV FLASK_APP=etl_project/src/main.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]