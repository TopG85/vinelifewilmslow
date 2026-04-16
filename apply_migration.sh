#!/bin/bash
cd '/Users/danielcarson/Documents/Visual Studio Code Project/Vinelife Wilmslow/vinelifewilmslow'
mv core/models_fixed.py core/models.py
source venv/bin/activate
python manage.py makemigrations
python manage.py migrate
