import os
import sys
import time
from pprint import pprint

import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator, PythonVirtualenvOperator
from airflow_utils import set_dag_id

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


def print_context(ds, **kwargs):
    """Print the Airflow context and ds variable from the context."""
    pprint(kwargs)
    print(ds)
    return "Whatever you return gets printed in the logs"


def my_sleeping_function(random_base):
    """This is a function that will run within the DAG execution"""
    time.sleep(random_base)


def callable_virtualenv():
    """
    Example function that will be performed in a virtual environment.

    Importing at the module level ensures that it will not attempt to import the
    library before it is installed.
    """
    from time import sleep

    from colorama import Back, Fore, Style

    print(Fore.RED + "some red text")
    print(Back.GREEN + "and with a green background")
    print(Style.DIM + "and in dim text")
    print(Style.RESET_ALL)
    for _ in range(10):
        print(Style.DIM + "Please wait...", flush=True)
        sleep(10)
    print("Finished")


with DAG(
    dag_id=set_dag_id(__file__), start_date=pendulum.datetime(2025, 1, 1, tz="UTC"), schedule=None
) as dag:
    run_this = BashOperator(task_id="bash_run_after_loop", bash_command="echo 1")

    also_run_this = BashOperator(
        task_id="bash_also_run_this",
        bash_command='echo "run_id={{ run_id }} | dag_run={{ dag_run }}"',
    )

    bash_task = BashOperator(
        task_id="bash_task",
        bash_command="echo \"here is the message: '$message'\"",
        env={"message": '{{ "olá" if dag_run else "" }}'},
    )

    run_this_p = PythonOperator(
        task_id="python_print_the_context", python_callable=print_context
    )

    # Generate 5 sleeping tasks, sleeping from 0.0 to 0.4 seconds respectively
    for i in range(5):
        task = PythonOperator(
            task_id="sleep_for_" + str(i),
            python_callable=my_sleeping_function,
            op_kwargs={"random_base": float(i) / 10},
        )

        run_this_p >> task

    virtualenv_task = PythonVirtualenvOperator(
        task_id="virtualenv_python",
        python_callable=callable_virtualenv,
        requirements=["colorama==0.4.0"],
        system_site_packages=False,
    )
