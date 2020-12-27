import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago

from airflow_utils import set_dag_id


with DAG(dag_id=set_dag_id(__file__), schedule_interval=None, start_date=days_ago(1)) as dag:
    start = DummyOperator(task_id='start')
    do_something = DummyOperator(task_id='do_something')
    end = DummyOperator(task_id='end')

    start >> do_something >> end
