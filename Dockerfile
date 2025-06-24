FROM apache/airflow:3.0.2-python3.12

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt
