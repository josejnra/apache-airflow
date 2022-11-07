FROM apache/airflow:2.4.2-python3.9

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt
