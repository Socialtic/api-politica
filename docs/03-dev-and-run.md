#   Run and dev

## Components

- `python3`
- `pip3`
- `virtualenv`
- `flask`

##   Running app

### Setup environment

This development was made on Debian/Ubuntu GNU/Linux based distro. Please verify any command for your distro before
execute it.

####    Setting up `virtualenv` and `python3`

```bash
# Create a virtual environment.
virtualenv venv -p /usr/bin/python3

# Activate virtual environment
source ./venv/bin/activate

# To deactivate the virtual environment
deactivate
```

####    Installing dependencies

```bash
pip install -r ./requirements.txt
```

####    Running

```bash
# Running app
python ./application.py
```

Now you can go to [localhost:500](localhost:500).

##  Dev

The current configuration is on the [/app/__init__.py](../app/__init__.py) file.

You can set up the DB with the `database_file` variable.

To enable the dev mode and get the `post`, `put` and `delete` methods available you need to change the 
`isOnDev` var to `True`. To revert this and get only enable the `get` method, change the `isOnDev` to `False`. 

To change the port or host where the apps is running, you can modify the [application.py](../application.py) file.