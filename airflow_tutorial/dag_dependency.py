import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import pendulum
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.sensors.external_task import ExternalTaskMarker, ExternalTaskSensor
from airflow_utils import set_dag_id

with DAG(
    dag_id=set_dag_id(__file__) + "-parent",
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    schedule="@daily",
) as parent_dag:
    start = EmptyOperator(task_id="start")

    do_something = BashOperator(task_id="do_something", bash_command="sleep 10s")

    # Use Task Marker in case to clear child task if this task is cleared
    end = ExternalTaskMarker(
        task_id="end",
        external_dag_id="dag-dependency-child",
        external_task_id="child_task1",
    )

    start >> do_something >> end


with DAG(
    dag_id=set_dag_id(__file__) + "-child",
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    schedule="@daily",
) as child_dag:
    child_task1 = ExternalTaskSensor(
        task_id="child_task1",
        external_dag_id=parent_dag.dag_id,
        external_task_id=end.task_id,
        timeout=600,
        allowed_states=["success"],
        failed_states=["failed", "skipped"],
        mode="reschedule",
    )
