# open-elections-mx-2021

API abierta para consultar a los y las candidatas de las elecciones de México 2021

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
# Running server
python ./main.py

# Testing
python ./test.py
```
