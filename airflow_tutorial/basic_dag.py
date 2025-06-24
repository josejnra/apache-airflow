import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import pendulum
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow_utils import set_dag_id

with DAG(
    dag_id=set_dag_id(__file__), schedule="@daily", start_date=pendulum.datetime(2021, 1, 1, tz="UTC")
) as dag:
    start = EmptyOperator(task_id="start")
    do_something = EmptyOperator(task_id="do_something")
    end = EmptyOperator(task_id="end")

    start >> do_something >> end
