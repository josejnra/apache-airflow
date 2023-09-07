import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.utils.dates import days_ago

from airflow_utils import set_dag_id


with DAG(dag_id=set_dag_id(__file__), schedule_interval="@daily", start_date=days_ago(3)) as dag:
    start = EmptyOperator(task_id='start')
    do_something = EmptyOperator(task_id='do_something')
    end = EmptyOperator(task_id='end')

    start >> do_something >> end
