import os
import sys

from airflow.operators.python import PythonOperator

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import pendulum
from airflow import DAG
from airflow.models.baseoperator import BaseOperator
from airflow_utils import set_dag_id


class TesteOperator(BaseOperator):
    template_fields = ["param1", "param2"]

    def __init__(self, param1: str, param2: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.param1 = param1
        self.param2 = param2 if param2.endswith("db") else param2 + ".adiciona"

    def execute(self, context):
        message = f"Valor de PARAM1: {self.param1 if self.param1.endswith('ela') else self.param1 + '.adiciona'}"
        self.log.info(message)
        message = f"Valor de PARAM2: {self.param2}"
        self.log.info(message)


def func1(task_instance):
    task_instance.xcom_push(key="table_name", value="minha_tabela")
    task_instance.xcom_push(key="db_name", value="meu_db")


with DAG(
    dag_id=set_dag_id(__file__),
    schedule=None,
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    tags=["xcom"],
) as dag:
    op1 = PythonOperator(task_id="gerar_vars", python_callable=func1)

    op2 = TesteOperator(
        task_id="usar_vars",
        param1="{{ task_instance.xcom_pull(task_ids='gerar_vars', key='table_name') }}",
        param2="{{ task_instance.xcom_pull(task_ids='gerar_vars', key='db_name') }}",
    )

    op1 >> op2
