#!/usr/bin/env python
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vinelife_cms.settings')
sys.path.insert(0, os.path.dirname(__file__))
django.setup()

from wagtail.models import Page
from core.models import HomePage

# Get root page
root = Page.objects.get(pk=1)
print(f"Root page: {root.title}")

# Check if HomePage already exists
existing = HomePage.objects.exists()
if existing:
    print("HomePage already exists")
    sys.exit(0)

# Try to create HomePage using Wagtail's method
try:
    home = HomePage(title='Vinelife Wilmslow', slug='home')
    root.add_child(instance=home)
    home.save_revision().publish()
    print("✅ HomePage created and published!")
except Exception as e:
    print(f"Error using add_child: {e}")
    print("\nTrying alternative approach...")
    
    # Alternative: Create with manual path calculation
    try:
        home = HomePage(title='Vinelife Wilmslow', slug='home')
        home.path = '00010001'
        home.depth = 2
        home.save()
        home.save_revision().publish()
        print("✅ HomePage created (alternative method)!")
    except Exception as e2:
        print(f"Error: {e2}")
        sys.exit(1)

print("Homepage is ready!")
print("Visit: http://127.0.0.1:8000/")
