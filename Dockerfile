FROM python:3.13-slim
COPY app.py /
CMD ["python3", "/app.py"]