## Poetry
### Install Poetry
If you don't have poetry installed, just execute:
```shell script
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```
If anything wrong happens, check the [docs](https://python-poetry.org/docs/).

### Create env
If you have python3.7 on your machine, just run the code below to create a new env for this project.
```shell script
$ poetry env use python3.7
```
You may check the others envs by running:
```shell script
$ poetry env list
```

### Install Project Dependencies
In order to install the project dependencies you all need is just run:
```shell script
$ poetry install
```
