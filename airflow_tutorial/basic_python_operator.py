import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow_utils import set_dag_id

with DAG(
    dag_id=set_dag_id(__file__), start_date=pendulum.datetime(2025, 1, 1, tz="UTC"), schedule=None
) as dag:

    def say_hello():
        print("Hello, guys! Your are the best!")

    PythonOperator(task_id="say_hello", python_callable=say_hello)
