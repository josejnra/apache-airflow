FROM apache/airflow:2.2.5-python3.9

USER root

RUN chmod g+w /home/airflow

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

USER airflow
