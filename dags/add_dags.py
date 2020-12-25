import os

from airflow.models import DagBag

dags_dirs = os.getenv('DAGS_FOLDER').split(',') if os.getenv('DAGS_FOLDER') else []

for directory in dags_dirs:
    dag_bag = DagBag(os.path.expanduser(directory))

    if dag_bag:
        for dag_id, dag in dag_bag.dags.items():
            globals()[dag_id] = dag
