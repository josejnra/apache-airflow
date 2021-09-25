For this project you must have installed Docker and docker-compose.

## Poetry
### Install Poetry
If you don't have poetry already installed, just execute:
```shell
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```
If anything wrong happens, check the [docs](https://python-poetry.org/docs/).

### Create env
If you have python3.7 on your machine, just run the code below to create a new env for this project.
```shell script
poetry env use python3.7
```
You may check the others envs by running:
```shell
poetry env list
```

### Export requirements.txt
If you prefer to work the old way, with requirements.txt, you may export it with:
```shell
poetry export --without-hashes -o requirements.txt
```

### Install Project Dependencies
In order to install the project dependencies you all need is just run:
```shell script
poetry install
```


## How to Run
First you have to set airflow user id and group id by running:
```shell
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" >> .env
```

Then, just initialize the database to use:
```shell
docker-compose up initdb
```
All configuration parameters are set in [.env](.env) file.

The last command, in order to run all services is:
```shell
docker-compose up -d
```

### Metrics
Access metrics at [here](http://localhost:9102/metrics).

### DAGs
If you want to add DAGs, all you have to do is to mount a volume of your DAGs on __x-dags-and-logs__ anchor on the [yaml file](docker-compose.yml).
After that, just update the __DAG_FOLDERS__ environment variable on __x-airflow-env__ anchor to notify airflow where to get the new DAGs.
