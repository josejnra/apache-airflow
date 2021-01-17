import logging
import os
import sys


sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults

from airflow_utils import set_dag_id


class HelloOperator(BaseOperator):

    @apply_defaults
    def __init__(
            self,
            name: str,
            **kwargs) -> None:
        super().__init__(**kwargs)
        self.name = name

    def execute(self, context):
        message = "Hello {}".format(self.name)
        logging.info(message)
        return message


with DAG(dag_id=set_dag_id(__file__), start_date=days_ago(1), schedule_interval="@daily") as parent_dag:

    hello_task = HelloOperator(task_id='sample-task', name='foo_bar')
