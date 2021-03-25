FROM apache/airflow:2.0.1-python3.8

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt
