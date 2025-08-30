#!/usr/bin/env python
"""
Script to check current pricing packages in Django
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'takweensoft_backend.settings')
django.setup()

from content_management.models import PricingPackage

def check_pricing_data():
    """Check current pricing packages"""
    
    print("🔍 Current Pricing Packages in Django:")
    print("=" * 50)
    
    packages = PricingPackage.objects.all().order_by('order')
    
    if not packages.exists():
        print("❌ No pricing packages found!")
        return
    
    for package in packages:
        print(f"📦 Package {package.order}:")
        print(f"   ID: {package.id}")
        print(f"   Name (AR): {package.name_ar}")
        print(f"   Name (EN): {package.name_en}")
        print(f"   Price: {package.price} {package.currency}")
        print(f"   Period: {package.period_ar}")
        print(f"   Active: {'✅' if package.is_active else '❌'}")
        print(f"   Popular: {'✅' if package.is_popular else '❌'}")
        print(f"   Features Count: {len(package.features_ar)}")
        print("-" * 30)
    
    print(f"\n📊 Total Packages: {packages.count()}")
    print(f"✅ Active Packages: {packages.filter(is_active=True).count()}")
    print(f"⭐ Popular Packages: {packages.filter(is_popular=True).count()}")

if __name__ == '__main__':
    check_pricing_data()
