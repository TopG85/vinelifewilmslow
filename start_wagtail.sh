#!/bin/bash#!/bin/bash




















python manage.py runserver 0.0.0.0:8000echo ""echo "🔐 Admin login: http://127.0.0.1:8000/admin"echo "📱 Access at: http://127.0.0.1:8000"echo "🚀 Starting Wagtail dev server..."echo ""EOF    print("✅ Superuser 'admin' already exists")else:    print("✅ Superuser created: admin / admin123")    User.objects.create_superuser('admin', 'admin@vinelife.local', 'admin123')if not User.objects.filter(username='admin').exists():from django.contrib.auth.models import Userpython manage.py shell << EOF# Check if superuser exists and create if notsource venv/bin/activatecd '/Users/danielcarson/Documents/Visual Studio Code Project/Vinelife Wilmslow/vinelifewilmslow'cd '/Users/danielcarson/Documents/Visual Studio Code Project/Vinelife Wilmslow/vinelifewilmslow'
source venv/bin/activate

# Check if superuser exists and create if not
python manage.py shell << EOF
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@vinelife.local', 'admin123')
    print("✅ Superuser created: admin / admin123")
else:
    print("✅ Superuser 'admin' already exists")
EOF

echo ""
echo "🚀 Starting Wagtail dev server..."
echo "📱 Access at: http://127.0.0.1:8000"
echo "🔐 Admin login: http://127.0.0.1:8000/admin"
echo ""
python manage.py runserver 0.0.0.0:8000
