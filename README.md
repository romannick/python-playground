## Simple Python flask crud API

### Run the project
1. `python3 -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `python -m src.app`

### DB migrations
1. `export FLASK_APP=src.app:create_app`
2. Init with `flask db init`
3. Create migration with `flask db migrate -m "Add new column price to Items"`
4. Run migrations with `flask db upgrade`