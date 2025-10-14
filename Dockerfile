FROM python:3.13-slim
COPY app.py /
COPY test.html /
EXPOSE 80
CMD ["python3", "/app.py"]
