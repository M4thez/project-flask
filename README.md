# Flask Todo application

## App description

Simple Todo application made in the Flask framework. App allows to add new notes, delete existing ones and mark them as complete. Notes are stored in SQLite database and are persistent across sessions.

## Usage

To run with Docker type 
'''
docker compose up
'''
Application should now be running on
'''
localhost:5000
'''

To run without Docker, but with Python and pip type
'''
pip install -r req.txt
'''
and then
'''
python app.py
'''
to run with debug mode on and application openly available on your network

or
'''
flask run
'''
to run with debug mode off and only on your local machine

Application should now be running on
'''
localhost:5000
'''