import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup

from airflow_utils import set_dag_id

with DAG(dag_id=set_dag_id(__file__),
         start_date=days_ago(1),
         schedule_interval=None) as dag:

    start = BashOperator(
       task_id="start",
       bash_command="echo start",
    )

    end = BashOperator(
       task_id="end",
       bash_command="echo end",
    )

    with TaskGroup(group_id="tasks_group_1") as tg1:
        previous_echo = BashOperator(
           task_id="task_1",
           bash_command="echo task 1"
        )
        for i in range(2, 6):
            next_echo = BashOperator(task_id=f"task_{i}",
                                     bash_command=f"echo task {i}")
            previous_echo >> next_echo
            previous_echo = next_echo

    with TaskGroup(group_id="tasks_group_2") as tg2:
        previous_echo = BashOperator(
           task_id="task_1",
           bash_command="echo task 1"
        )
        for i in range(2, 6):
            next_echo = BashOperator(
               task_id=f"task_{i}",
               bash_command=f"echo task {i}"
            )
            previous_echo >> next_echo
            previous_echo = next_echo

    start >> [tg1, tg2] >> end
