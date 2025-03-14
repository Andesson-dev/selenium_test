FROM python:latest

WORKDIR app

RUN pip install selenium

COPY . .

CMD ["python", "main.py"]
