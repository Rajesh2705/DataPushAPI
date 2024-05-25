1. Create a Virtuval Env named .venv

    python3 -m venv .venv

2. Activate Virtuval Env using the command

    source .venv/bin/activate

3. Install Packges using requirement.txt file
    python3 -m pip install -r requirement.txt

4. Create Project base
    django-admin startproject base
5. cd to base and create app datapush
    cd base && python3 manage.py startapp datapush