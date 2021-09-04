FROM apache/airflow:2.1.3-python3.9

USER root

RUN chmod g+w /home/airflow

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

USER airflow
