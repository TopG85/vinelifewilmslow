#!/usr/bin/env python
import os
import django
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vinelife_cms.settings')
django.setup()

from django.contrib.auth.models import User

# Get credentials from environment variables
username = os.getenv('SUPERUSER_USERNAME', 'admin')
email = os.getenv('SUPERUSER_EMAIL', 'admin@vinelife.local')
password = os.getenv('SUPERUSER_PASSWORD', 'admin123')

# Delete existing user if it exists
User.objects.filter(username=username).delete()

# Create new superuser
user = User.objects.create_superuser(username, email, password)
print("✅ Superuser created successfully!")
print(f"Username: {username}")
print(f"Email: {email}")
print("\nLogin at: http://127.0.0.1:8002/admin/")
print("\n📝 Note: Credentials are loaded from environment variables (.env file)")
