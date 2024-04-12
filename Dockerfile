FROM apache/airflow:2.9.0-python3.11

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt
