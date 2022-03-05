import json
import os
import sys
import pathlib

from airflow.operators.python import PythonOperator

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from airflow import DAG
from airflow.utils.dates import days_ago

from airflow_utils import set_dag_id
from airflow.models.baseoperator import BaseOperator


DIR_PATH = pathlib.Path(__file__).parent.absolute()
PATH_CONFIG_JOBS = f"{DIR_PATH}/job_config.json"


class TesteOperator(BaseOperator):

    def __init__(
            self,
            param1: dict,
            **kwargs) -> None:
        super().__init__(**kwargs)
        self.param1 = param1

    def execute(self, context):
        message = f"Valor de PARAM1: {self.param1}"
        self.log.info(message)


def run_job(ds, job, initial_date, end_date):
    config_jobs = get_json(PATH_CONFIG_JOBS)
    config_job = config_jobs.get("generic_jobs")

    customs = {
        "initial_date": initial_date,
        "end_date": end_date,
        "job_path": config_job.get(job)["job_path"],
        "job_module": config_job.get(job)["job_module"]
    }

    TesteOperator(
        task_id="usar_params",
        param1=customs
    ).execute(ds)


def get_json(path):
    with open(path) as file:
        config = json.load(file)

    return config


# {
#   "job": "job_1",
#   "initial_date": "2021-09-21",
#   "end_date": "2021-09-03"
# }
with DAG(dag_id=set_dag_id(__file__),
         schedule_interval=None,
         start_date=days_ago(1),
         tags=["param"]) as dag:

    PythonOperator(
        task_id="run_job",
        python_callable=run_job,
        op_kwargs={
            "job": "{{ dag_run.conf['job'] }}",
            "initial_date": "{{ dag_run.conf['initial_date'] }}",
            "end_date": "{{ dag_run.conf['end_date'] }}"
        }
    )
