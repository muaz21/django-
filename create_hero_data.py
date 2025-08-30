#!/usr/bin/env python
"""
Script to create sample hero section data
Run with: python manage.py shell < create_hero_data.py
"""

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'takweensoft_backend.settings')
django.setup()

from content_management.models import HeroSection

def create_hero_data():
    """Create sample hero section data"""
    
    # Check if hero section already exists
    if HeroSection.objects.exists():
        print("Hero section already exists. Updating...")
        hero = HeroSection.objects.first()
    else:
        print("Creating new hero section...")
        hero = HeroSection()
    
    # Set the data
    hero.title_ar = "تطوير مواقع الويب الاحترافية"
    hero.title_en = "Professional Web Development"
    hero.subtitle_ar = "نحول أفكارك إلى مواقع رقمية مذهلة"
    hero.subtitle_en = "Transform Your Ideas Into Amazing Digital Experiences"
    hero.description_ar = "نقدم حلول تطوير الويب المتكاملة باستخدام أحدث التقنيات"
    hero.description_en = "We provide comprehensive web development solutions"
    hero.cta_text_ar = "ابدأ مشروعك الآن"
    hero.cta_text_en = "Start Your Project Now"
    hero.cta_url = "/contact"
    hero.is_active = True
    
    # Save the hero section
    hero.save()
    print(f"Hero section saved with ID: {hero.id}")
    print("Data created successfully!")

if __name__ == "__main__":
    create_hero_data()
