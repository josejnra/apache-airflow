import sys
import os
import random

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from airflow.models import DAG
from airflow.operators.python_operator import BranchPythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago


from airflow_utils import set_dag_id


def return_branch(**kwargs):
    branches = ['branch_0', 'branch_1', 'branch_2']
    return random.choice(branches)


with DAG(set_dag_id(__file__), schedule_interval=None, start_date=days_ago(1)) as dag:

    kick_off_dag = DummyOperator(task_id='run_this_first')

    branching = BranchPythonOperator(
        task_id='branching',
        python_callable=return_branch,
        provide_context=True)

    kick_off_dag >> branching

    for i in range(0, 3):
        dummpy_operator = DummyOperator(task_id='branch_{0}'.format(i))
        for j in range(0, 3):
            another_dummy_operator = DummyOperator(task_id='branch_{0}_{1}'.format(i, j))
            dummpy_operator >> another_dummy_operator
        branching >> dummpy_operator
