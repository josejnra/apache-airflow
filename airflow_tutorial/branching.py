import sys
import os
import random
from typing import Any

from airflow_utils import set_dag_id
from airflow.models import DAG
from airflow.operators.python import BranchPythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.utils.dates import days_ago

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


def return_branch() -> Any:
    branches = ['branch_0', 'branch_1', 'branch_2']
    return random.choice(branches)


with DAG(set_dag_id(__file__), schedule_interval=None, start_date=days_ago(1)) as dag:

    kick_off_dag = EmptyOperator(task_id='run_this_first')

    branching = BranchPythonOperator(
        task_id='branching',
        python_callable=return_branch,
        provide_context=True)

    kick_off_dag >> branching

    for i in range(0, 3):
        dummpy_operator = EmptyOperator(task_id=f'branch_{i}')
        for j in range(0, 3):
            another_dummy_operator = EmptyOperator(task_id=f'branch_{i}_{j}')
            dummpy_operator >> another_dummy_operator
        branching >> dummpy_operator
