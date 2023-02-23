FROM apache/airflow:2.5.1-python3.9

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt
