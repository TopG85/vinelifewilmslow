#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vinelife_cms.settings')
django.setup()

from django.contrib.auth.models import User

# Delete existing admin user if it exists
User.objects.filter(username='admin').delete()

# Create new superuser
user = User.objects.create_superuser('admin', 'admin@vinelife.local', 'admin123')
print("✅ Superuser created successfully!")
print("Username: admin")
print("Password: admin123")
print("\nLogin at: http://127.0.0.1:8002/admin/")
