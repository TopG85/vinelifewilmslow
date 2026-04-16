#!/bin/bash
cd '/Users/danielcarson/Documents/Visual Studio Code Project/Vinelife Wilmslow/vinelifewilmslow'
source venv/bin/activate

# Run migrations to set up database
echo "⚙️  Running database migrations..."
python manage.py migrate

# Remind user to create superuser if needed
echo "✓ Database setup complete"
echo ""
echo "📌 To create or update admin user, run:"
echo "   python manage.py createsuperuser"
echo ""
echo "🚀 Wagtail server starting at http://127.0.0.1:8000"
echo "📱 Admin: http://127.0.0.1:8000/admin"
echo "ℹ️  Log in with your superuser credentials"
echo "💡 Tip: Run 'python manage.py createsuperuser' if you need a new admin account"
python manage.py runserver 0.0.0.0:8000
