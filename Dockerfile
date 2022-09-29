FROM apache/airflow:2.4.0-python3.9

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt
