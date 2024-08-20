FROM apache/airflow:2.10.0-python3.11

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt
