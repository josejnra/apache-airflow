FROM apache/airflow:2.10.4-python3.11

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt
