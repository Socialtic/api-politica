# open-elections-mx-2021

API abierta para consultar a los y las candidatas de las elecciones de México 2021

# Database

##  ER model

Diagrams can be found in [docs folder](./docs).

- [XML version](./docs/mx-elections-2021-db-er-diagram.xml) from [diagrams.net](diagrams.net)
- [PNG version](./docs/mx-elections-2021-db-er-diagram.png)

![ER model](./docs/mx-elections-2021-db-er-diagram.png)

# Components

- `python3`
- `pip3`
- `virtualenv`
- `flask`

# Setup environment

This development was made on Debian/Ubuntu GNU/Linux based distro.
Please verify any command for your distro before execute it.

## Setting up `virtualenv` and `python3`

```bash
# Create a virtual environment.
virtualenv venv -p /usr/bin/python3

# Activate virtual environment
source ./venv/bin/activate

# To deactivate the virtual environment
deactivate
```

## Installing dependencies

```bash
pip install -r ./requirements.txt
```

# Running

```bash
# Running app
python ./run.py
```
