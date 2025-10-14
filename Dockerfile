FROM python:3.13-slim
COPY app.py /
EXPOSE 80
CMD ["python3", "/app.py"]
