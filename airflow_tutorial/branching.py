import os
import random
import sys

import pendulum
from airflow.decorators import task
from airflow.models import DAG
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow_utils import set_dag_id

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

with DAG(set_dag_id(__file__), schedule=None, start_date=pendulum.datetime(2025, 1, 1, tz="UTC")) as dag:
    kick_off_dag = EmptyOperator(task_id="run_this_first")

    branches = ["branch_0", "branch_1", "branch_2"]

    @task.branch(task_id="branching")
    def branch_func():
        chosen_option = random.choice(branches)
        return chosen_option

    branching = branch_func()

    kick_off_dag >> branching

    for i in range(0, 3):
        dummy_operator = EmptyOperator(task_id=f"branch_{i}")
        for j in range(0, 3):
            another_dummy_operator = EmptyOperator(task_id=f"branch_{i}_{j}")
            dummy_operator >> another_dummy_operator
        branching >> dummy_operator
