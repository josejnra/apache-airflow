import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.subdag import SubDagOperator
from airflow.utils.dates import days_ago
from airflow_utils import set_dag_id


def subdag_factory(parent_dag_name, child_dag_name, args) -> DAG:
    """
    Generate a DAG to be used as a subdag.

    :param str parent_dag_name: Id of the parent DAG
    :param str child_dag_name: Id of the child DAG
    :param dict args: Default arguments to provide to the subdag
    :return: DAG to use as a subdag
    :rtype: airflow.models.DAG
    """
    dag_subdag = DAG(
        dag_id=f"{parent_dag_name}.{child_dag_name}",
        default_args=args,
        schedule_interval="@daily",
    )

    for i in range(5):
        EmptyOperator(
            task_id="{}-task-{}".format(child_dag_name, i + 1),
            default_args=args,
            dag=dag_subdag,
        )

    return dag_subdag


# start date should be the same for parent dag and subdag. In order to all tasks have the same value.
default_args = {"start_date": days_ago(2)}

with DAG(
    dag_id=set_dag_id(__file__),
    default_args=default_args,
    schedule_interval="@once",
    tags=["example"],
) as dag:
    start = EmptyOperator(
        task_id="start",
        dag=dag,
    )

    section_1 = SubDagOperator(
        task_id="section-1",
        subdag=subdag_factory(set_dag_id(__file__), "section-1", default_args),
        dag=dag,
    )

    some_other_task = EmptyOperator(
        task_id="some-other-task",
        dag=dag,
    )

    section_2 = SubDagOperator(
        task_id="section-2",
        subdag=subdag_factory(set_dag_id(__file__), "section-2", default_args),
        dag=dag,
    )

    end = EmptyOperator(
        task_id="end",
        dag=dag,
    )

    start >> section_1 >> some_other_task >> section_2 >> end
