#!/bin/bash
cd '/Users/danielcarson/Documents/Visual Studio Code Project/Vinelife Wilmslow/vinelifewilmslow'
source venv/bin/activate

# Create superuser (non-interactive)
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@vinelife.local', 'admin123')" | python manage.py shell

# Start server
echo "🚀 Wagtail server starting at http://127.0.0.1:8000"
echo "📱 Admin: http://127.0.0.1:8000/admin"
echo "👤 Username: admin"
echo "🔑 Password: admin123"
python manage.py runserver 0.0.0.0:8000
