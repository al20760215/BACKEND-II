FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install flask
RUN pip install psycopg2-binary
RUN pip install Flask-Limiter
RUN mkdir -p /app/uploads && chmod 777 /app/uploads
EXPOSE 80
CMD ["python","app.py"]