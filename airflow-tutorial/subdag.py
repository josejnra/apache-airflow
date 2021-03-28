import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.subdag import SubDagOperator
from airflow.utils.dates import days_ago

from airflow_utils import set_dag_id


def subdag(parent_dag_name, child_dag_name, args):
    """
    Generate a DAG to be used as a subdag.

    :param str parent_dag_name: Id of the parent DAG
    :param str child_dag_name: Id of the child DAG
    :param dict args: Default arguments to provide to the subdag
    :return: DAG to use as a subdag
    :rtype: airflow.models.DAG
    """
    dag_subdag = DAG(
        dag_id=f'{parent_dag_name}.{child_dag_name}',
        default_args=args,
        start_date=days_ago(2),
        schedule_interval="@daily",
    )

    for i in range(5):
        DummyOperator(
            task_id='{}-task-{}'.format(child_dag_name, i + 1),
            default_args=args,
            dag=dag_subdag,
        )

    return dag_subdag


with DAG(
    dag_id=set_dag_id(__file__), start_date=days_ago(2), schedule_interval="@once", tags=['example']
) as dag:

    start = DummyOperator(
        task_id='start',
        dag=dag,
    )

    section_1 = SubDagOperator(
        task_id='section-1',
        subdag=subdag(set_dag_id(__file__), 'section-1', {}),
        dag=dag,
    )

    some_other_task = DummyOperator(
        task_id='some-other-task',
        dag=dag,
    )

    section_2 = SubDagOperator(
        task_id='section-2',
        subdag=subdag(set_dag_id(__file__), 'section-2', {}),
        dag=dag,
    )

    end = DummyOperator(
        task_id='end',
        dag=dag,
    )

    start >> section_1 >> some_other_task >> section_2 >> end
