#!/usr/bin/env python
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vinelife_cms.settings")
django.setup()

from core.models import HomePage

try:
    home = HomePage.objects.get(title="Home")
    print(f"Current HomePage slug: '{home.slug}'")
    print(f"Current HomePage path: {home.get_url()}")
    
    # Set slug to empty string for root URL
    home.slug = ""
    home.save()
    
    # Publish the page
    home.save_revision().publish()
    
    print(f"✅ HomePage slug updated to: '{home.slug}'")
    print(f"New HomePage path: {home.get_url()}")
except HomePage.DoesNotExist:
    print("❌ HomePage not found")
except Exception as e:
    print(f"❌ Error: {e}")
