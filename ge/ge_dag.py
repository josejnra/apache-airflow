import os
from datetime import datetime
from pathlib import Path

from airflow import DAG

from great_expectations_provider.operators.great_expectations import GreatExpectationsOperator

base_path = Path(__file__).parents[0]  # /home/airflow/ge
data_dir = os.path.join(base_path, "data")

ge_root_dir = os.path.join(base_path, "great_expectations")


with DAG(
        dag_id="great_expectations_dag",
        start_date=datetime(2021, 12, 15),
        catchup=False,
        schedule_interval=None
) as dag:
    ge_data_context_root_dir_with_checkpoint_name_pass = GreatExpectationsOperator(
        task_id="ge_checkpoint_titanic",
        data_context_root_dir=ge_root_dir,
        checkpoint_name="titanic_checkpoint",
    )
