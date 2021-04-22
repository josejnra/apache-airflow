FROM apache/airflow:2.0.2-python3.8

USER root

RUN chmod g+w /home/airflow

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

USER airflow
