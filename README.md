For this project you must have installed Docker and docker-compose.

## Poetry
### Install Poetry
If you don't have poetry already installed, just execute:
```shell
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```
If anything wrong happens, check the [docs](https://python-poetry.org/docs/).

### Create env
If you have python3.7 on your machine, just run the code below to create a new env for this project.
```shell script
$ poetry env use python3.7
```
You may check the others envs by running:
```shell
$ poetry env list
```

### Export requirements.txt
If you prefer to work the old way, with requirements.txt, you may export it with:
```shell
$ poetry export --without-hashes -o requirements.txt
```

### Install Project Dependencies
In order to install the project dependencies you all need is just run:
```shell script
$ poetry install
```


## Run project locally
First you have to change the __database__ and logs folder permission with the followings command:
```shell
sudo chown -R 1001:0 database
sudo chmod -R 777 logs
```

Then, just setup the databases you want to use:
```shell
docker-compose up pgdb mysqldb initdb
```
In this case I set up two databases, just for fun. But you can only work with one based
on what you have defined in [.env](.env) file.

The next step is to uncomment the `initdb` service on [doker-compose](docker-compose.yml).
Thus, after initialized the database you should comment again this service in order to guarantee that 
you will not initialize the database again or create the same user.

The last comando to run all services is:
```shell
docker-compose up -d
```