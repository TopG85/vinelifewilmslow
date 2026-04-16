#!/usr/bin/env python
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vinelife_cms.settings")
django.setup()

from core.models import HomePage
from wagtail.models import Page

# Check all pages
print("=== ALL PAGES ===")
for page in Page.objects.all():
    print(f"Title: {page.title}, Slug: '{page.slug}', URL: {page.get_url() if hasattr(page, 'get_url') else 'N/A'}, Live: {page.live}")

print("\n=== HOME PAGES ===")
for home in HomePage.objects.all():
    print(f"Title: {home.title}, Slug: '{home.slug}', Live: {home.live}")
    print(f"URL path: {home.get_url() if hasattr(home, 'get_url') else 'N/A'}")
