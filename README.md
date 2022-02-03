# Flask Todo application

## App description

Simple Todo application made in the Flask framework. 

App allows to add new notes, delete existing ones or mark them as complete. Notes are stored in SQLite database and are persistent across sessions.

## Usage

To run with Docker type 
```
docker compose up
```
Application should now be running on
```
localhost:5000
```

To run without Docker (but with Python and pip) type
```
pip install -r req.txt
```
and then
```
python app.py
```
Application now runs with debug mode on and is openly available on your local network

To access it type
```
localhost:5000
```

Alternatively use (runs with debug mode off and only on your local machine)
```
flask run
```

To access it type
```
localhost:5000
```