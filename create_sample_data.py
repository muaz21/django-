#!/usr/bin/env python
"""
Script to create sample data for the Takween Soft website
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'takweensoft_backend.settings')
django.setup()

from content_management.models import Portfolio, Service, BlogPost, PricingPackage, HeroSection
from datetime import date, datetime

def create_portfolio_data():
    """Create sample portfolio projects"""
    
    # Clear existing data
    Portfolio.objects.all().delete()
    
    # Create portfolio projects
    projects = [
        {
            'title_ar': 'نظام تكوين سوفت الإداري',
            'title_en': 'Takweensoft Management System',
            'description_ar': 'نظام إدارة متكامل لإدارة المشاريع والعملاء مع تقارير متقدمة',
            'description_en': 'Integrated management system for project and client management with advanced reporting',
            'client_challenge_ar': 'تطوير نظام إداري شامل يلبي احتياجات الشركة المتنامية',
            'client_challenge_en': 'Develop comprehensive administrative system meeting growing company needs',
            'solution_ar': 'نظام ويب متطور مع قاعدة بيانات محسنة وواجهة مستخدم متجاوبة',
            'solution_en': 'Advanced web system with optimized database and responsive user interface',
            'features_ar': ['إدارة المشاريع', 'تتبع العملاء', 'التقارير المالية', 'إدارة الفرق'],
            'features_en': ['Project Management', 'Client Tracking', 'Financial Reports', 'Team Management'],
            'technologies': ['React.js', 'Django', 'PostgreSQL', 'Cloud Hosting'],
            'category': 'system',
            'live_url': 'https://system.takweensoft.com',
            'is_featured': True,
            'is_active': True,
            'order': 1,
            'completed_date': date(2024, 3, 10)
        },
        {
            'title_ar': 'موقع دات إكس ساي',
            'title_en': 'DatXSci Website',
            'description_ar': 'منصة متقدمة لعلوم البيانات والذكاء الاصطناعي تقدم حلول متكاملة للشركات',
            'description_en': 'Advanced data science and AI platform providing integrated solutions for businesses',
            'client_challenge_ar': 'تطوير منصة شاملة لعلوم البيانات مع واجهة سهلة الاستخدام',
            'client_challenge_en': 'Develop comprehensive data science platform with user-friendly interface',
            'solution_ar': 'بناء منصة متطورة باستخدام Vue.js مع أدوات تحليل البيانات المتقدمة',
            'solution_en': 'Built advanced platform using Vue.js with sophisticated data analysis tools',
            'features_ar': ['تحليل البيانات المتقدم', 'الذكاء الاصطناعي', 'واجهة تفاعلية', 'تقارير شاملة'],
            'features_en': ['Advanced Data Analysis', 'Artificial Intelligence', 'Interactive Interface', 'Comprehensive Reports'],
            'technologies': ['Vue.js', 'Node.js', 'AI/ML', 'Data Science'],
            'category': 'website',
            'live_url': 'https://datxsci.com',
            'is_featured': True,
            'is_active': True,
            'order': 2,
            'completed_date': date(2024, 1, 15)
        },
        {
            'title_ar': 'منصة إي بلات إكس',
            'title_en': 'EplatX Platform',
            'description_ar': 'منصة تجارة إلكترونية متكاملة مع أنظمة دفع متقدمة وحلول سحابية',
            'description_en': 'Integrated e-commerce platform with advanced payment systems and cloud solutions',
            'client_challenge_ar': 'إنشاء منصة تجارة إلكترونية قابلة للتوسع مع نظام دفع آمن',
            'client_challenge_en': 'Create scalable e-commerce platform with secure payment system',
            'solution_ar': 'تطوير منصة شاملة باستخدام React.js مع تكامل أنظمة الدفع المتعددة',
            'solution_en': 'Developed comprehensive platform using React.js with multiple payment system integration',
            'features_ar': ['نظام دفع متقدم', 'إدارة المخزون', 'لوحة تحكم شاملة', 'تطبيق الجوال'],
            'features_en': ['Advanced Payment System', 'Inventory Management', 'Comprehensive Dashboard', 'Mobile App'],
            'technologies': ['React.js', 'E-commerce', 'Payment Systems', 'Cloud'],
            'category': 'ecommerce',
            'live_url': 'https://eplatx.com',
            'is_featured': False,
            'is_active': True,
            'order': 3,
            'completed_date': date(2024, 2, 20)
        }
    ]
    
    for project_data in projects:
        Portfolio.objects.create(**project_data)
    
    print(f"✅ Created {len(projects)} portfolio projects")

def create_service_data():
    """Create sample services"""
    
    # Clear existing data
    Service.objects.all().delete()
    
    services = [
        {
            'title_ar': 'تطوير تطبيقات الويب',
            'title_en': 'Web Application Development',
            'description_ar': 'نطور تطبيقات ويب متقدمة باستخدام أحدث التقنيات',
            'description_en': 'We develop advanced web applications using cutting-edge technologies',
            'features_ar': ['React.js', 'Vue.js', 'Node.js', 'تصميم متجاوب'],
            'features_en': ['React.js', 'Vue.js', 'Node.js', 'Responsive Design'],
            'category': 'development',
            'icon_name': 'CodeIcon',
            'is_featured': True,
            'is_active': True,
            'order': 1
        },
        {
            'title_ar': 'تطوير التطبيقات المحمولة',
            'title_en': 'Mobile App Development',
            'description_ar': 'نبني تطبيقات محمولة لأندرويد و iOS',
            'description_en': 'We build mobile applications for Android and iOS',
            'features_ar': ['React Native', 'Flutter', 'iOS', 'Android'],
            'features_en': ['React Native', 'Flutter', 'iOS', 'Android'],
            'category': 'development',
            'icon_name': 'MobileIcon',
            'is_featured': True,
            'is_active': True,
            'order': 2
        },
        {
            'title_ar': 'التجارة الإلكترونية',
            'title_en': 'E-commerce Solutions',
            'description_ar': 'حلول تجارة إلكترونية متكاملة للشركات',
            'description_en': 'Integrated e-commerce solutions for businesses',
            'features_ar': ['متاجر إلكترونية', 'أنظمة الدفع', 'إدارة المخزون', 'التقارير'],
            'features_en': ['Online Stores', 'Payment Systems', 'Inventory Management', 'Reports'],
            'category': 'development',
            'icon_name': 'ShoppingIcon',
            'is_featured': False,
            'is_active': True,
            'order': 3
        }
    ]
    
    for service_data in services:
        Service.objects.create(**service_data)
    
    print(f"✅ Created {len(services)} services")

if __name__ == '__main__':
    print("🚀 Creating sample data for Takween Soft website...")
    
    create_portfolio_data()
    create_service_data()
    
    print("✅ Sample data created successfully!")
    print("\n🎯 You can now:")
    print("1. Visit: http://127.0.0.1:8000/admin/")
    print("2. Check API: http://127.0.0.1:8000/api/portfolio/")
    print("3. View your React website to see the new data!")
