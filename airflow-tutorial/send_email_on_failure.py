import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import task

from airflow_utils import set_dag_id

args = {
    'owner': 'email-tester',
    'description': 'Sending email test.',
    'start_date': days_ago(1),
    'email': ['my@email.com'],
    'email_on_failure': True
}


@task
def get_some_value():
    return 'My return'


@task
def raise_exception(text: str):
    raise Exception(text)


with DAG(dag_id=set_dag_id(__file__),
         default_args=args,
         schedule_interval=None) as dag:

    raise_exception(get_some_value())
