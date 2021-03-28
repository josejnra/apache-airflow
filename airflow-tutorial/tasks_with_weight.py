import os
import sys

from airflow.operators.dummy import DummyOperator

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

from airflow_utils import set_dag_id


with DAG(dag_id=set_dag_id(__file__), start_date=days_ago(1), schedule_interval=None) as dag:

    start = DummyOperator(task_id='start')

    task_1 = BashOperator(
        task_id='task_1',
        bash_command='echo task 1',
        pool="pool_tasks_weight_1",
        priority_weight=1
    )

    task_2 = BashOperator(
        task_id='task_2',
        bash_command='echo task 2',
        pool="pool_tasks_weight_2",
        priority_weight=2
    )

    task_3 = BashOperator(
        task_id='task_3',
        bash_command='echo task 3',
        pool="pool_tasks_weight_2",
        priority_weight=2
    )

    start >> task_1
    start >> task_2
    start >> task_3
