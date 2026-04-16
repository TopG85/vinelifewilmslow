#!/usr/bin/env python
"""
Apply pending migrations for the Vinelife CMS project.
This script creates and applies migrations for new fields.
"""
import os
import sys
import django
import subprocess

# Set up Django
os.chdir('/Users/danielcarson/Documents/Visual Studio Code Project/Vinelife Wilmslow/vinelifewilmslow')
sys.path.insert(0, os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vinelife_cms.settings')

print("🔧 Setting up Django...")
django.setup()

print("\n📋 Step 1: Creating migrations...")
result = subprocess.run([
    sys.executable, 'manage.py', 'makemigrations', 'core'
], capture_output=True, text=True)

print(result.stdout)
if result.stderr:
    print("STDERR:", result.stderr)

if result.returncode != 0:
    print(f"❌ makemigrations failed with code {result.returncode}")
    sys.exit(1)

print("\n✅ Step 2: Applying migrations...")
result = subprocess.run([
    sys.executable, 'manage.py', 'migrate'
], capture_output=True, text=True)

print(result.stdout)
if result.stderr:
    print("STDERR:", result.stderr)

if result.returncode != 0:
    print(f"❌ migrate failed with code {result.returncode}")
    sys.exit(1)

print("\n✅ Migrations applied successfully!")
print("🎉 Database schema is now up to date.")
