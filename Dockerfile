FROM python:3.11-slim-bullseye

WORKDIR /etl

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 3000

CMD ["python", "etl_process.py"]