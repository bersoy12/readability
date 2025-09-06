FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install flask readability-lxml requests

EXPOSE 5000

CMD ["python", "readability_server.py"]
