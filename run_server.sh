#!/bin/bash
cd '/Users/danielcarson/Documents/Visual Studio Code Project/Vinelife Wilmslow/vinelifewilmslow'
source venv/bin/activate  
rm -f db.sqlite3
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
