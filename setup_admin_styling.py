#!/usr/bin/env python
"""
Setup script for Django Admin Styling
This script helps set up the custom admin styling for Takween Soft
"""

import os
import sys
import django
from pathlib import Path

# Add the project directory to Python path
project_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(project_dir))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'takweensoft_backend.settings')
django.setup()

from django.core.management import call_command
from django.conf import settings

def setup_admin_styling():
    """Set up the custom admin styling"""
    print("🚀 Setting up Django Admin Styling...")
    
    # Check if templates directory exists
    templates_dir = project_dir / 'templates'
    if not templates_dir.exists():
        print("❌ Templates directory not found!")
        return False
    
    # Check if static directory exists
    static_dir = project_dir / 'static'
    if not static_dir.exists():
        print("❌ Static directory not found!")
        return False
    
    print("✅ Directories found")
    
    # Collect static files
    try:
        print("📦 Collecting static files...")
        call_command('collectstatic', '--noinput', '--clear')
        print("✅ Static files collected successfully")
    except Exception as e:
        print(f"❌ Error collecting static files: {e}")
        return False
    
    # Check if admin templates exist
    admin_templates = [
        'templates/admin/base_site.html',
        'templates/admin/index.html',
        'templates/admin/login.html',
        'templates/admin/change_form.html',
        'templates/admin/change_list.html',
    ]
    
    missing_templates = []
    for template in admin_templates:
        if not (project_dir / template).exists():
            missing_templates.append(template)
    
    if missing_templates:
        print(f"❌ Missing templates: {', '.join(missing_templates)}")
        return False
    
    print("✅ All admin templates found")
    
    # Check if CSS file exists
    css_file = project_dir / 'static' / 'admin' / 'css' / 'custom_admin.css'
    if not css_file.exists():
        print("❌ Custom CSS file not found!")
        return False
    
    print("✅ Custom CSS file found")
    
    print("\n🎉 Django Admin Styling setup completed successfully!")
    print("\n📋 What was set up:")
    print("   • Custom admin templates")
    print("   • Modern CSS styling")
    print("   • Responsive design")
    print("   • Enhanced admin interface")
    print("   • Custom admin configuration")
    
    print("\n🌐 To see the changes:")
    print("   1. Make sure your Django server is running")
    print("   2. Visit http://127.0.0.1:8000/admin/")
    print("   3. Log in with your admin credentials")
    
    print("\n💡 Features added:")
    print("   • Modern gradient header")
    print("   • Dashboard statistics cards")
    print("   • Improved navigation sidebar")
    print("   • Better form styling")
    print("   • Responsive design for mobile")
    print("   • Enhanced button and table styling")
    
    return True

if __name__ == '__main__':
    try:
        setup_admin_styling()
    except Exception as e:
        print(f"❌ Setup failed: {e}")
        sys.exit(1)
