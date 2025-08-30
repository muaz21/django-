#!/usr/bin/env python
import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'takweensoft_backend.settings')
django.setup()

from content_management.models import Service

def create_sample_services():
    """Create sample services for testing"""
    
    # Check if services already exist
    if Service.objects.exists():
        print("Services already exist in database.")
        print("Existing services:")
        for service in Service.objects.all():
            print(f"- {service.title_en} ({service.category})")
        return
    
    # Sample services data
    sample_services = [
        {
            'title_ar': 'تطوير تطبيقات الويب',
            'title_en': 'Web Application Development',
            'description_ar': 'تطوير تطبيقات ويب متقدمة ومتجاوبة باستخدام أحدث التقنيات',
            'description_en': 'Advanced and responsive web application development using cutting-edge technologies',
            'features_ar': ['تصميم متجاوب', 'أمان عالي', 'أداء محسن', 'قابلية التوسع'],
            'features_en': ['Responsive Design', 'High Security', 'Optimized Performance', 'Scalability'],
            'category': 'development',
            'icon_name': 'web',
            'is_featured': True,
            'is_active': True,
            'order': 1
        },
        {
            'title_ar': 'تطوير تطبيقات الهاتف المحمول',
            'title_en': 'Mobile App Development',
            'description_ar': 'تطوير تطبيقات الهاتف المحمول لنظامي iOS و Android',
            'description_en': 'Mobile application development for iOS and Android platforms',
            'features_ar': ['تصميم أصلي', 'تجربة مستخدم ممتازة', 'أداء عالي', 'دعم متعدد المنصات'],
            'features_en': ['Native Design', 'Excellent UX', 'High Performance', 'Cross-platform Support'],
            'category': 'development',
            'icon_name': 'mobile',
            'is_featured': True,
            'is_active': True,
            'order': 2
        },
        {
            'title_ar': 'تصميم الهوية البصرية',
            'title_en': 'Visual Identity Design',
            'description_ar': 'تصميم هوية بصرية مميزة ومتسقة للعلامات التجارية',
            'description_en': 'Distinctive and consistent visual identity design for brands',
            'features_ar': ['شعارات مميزة', 'ألوان متناسقة', 'خطوط احترافية', 'دليل هوية شامل'],
            'features_en': ['Distinctive Logos', 'Cohesive Colors', 'Professional Typography', 'Comprehensive Style Guide'],
            'category': 'design',
            'icon_name': 'design',
            'is_featured': True,
            'is_active': True,
            'order': 1
        },
        {
            'title_ar': 'حلول التجارة الإلكترونية',
            'title_en': 'E-commerce Solutions',
            'description_ar': 'تطوير منصات تجارة إلكترونية متكاملة ومتطورة',
            'description_en': 'Development of integrated and advanced e-commerce platforms',
            'features_ar': ['إدارة المنتجات', 'نظام دفع آمن', 'إدارة المخزون', 'تقارير متقدمة'],
            'features_en': ['Product Management', 'Secure Payment System', 'Inventory Management', 'Advanced Reports'],
            'category': 'development',
            'icon_name': 'shop',
            'is_featured': True,
            'is_active': True,
            'order': 3
        },
        {
            'title_ar': 'تحسين محركات البحث',
            'title_en': 'Search Engine Optimization',
            'description_ar': 'تحسين المواقع لمحركات البحث لزيادة الظهور والمرور',
            'description_en': 'Website optimization for search engines to increase visibility and traffic',
            'features_ar': ['تحليل الكلمات المفتاحية', 'تحسين المحتوى', 'تحليل الأداء', 'تقارير شهرية'],
            'features_en': ['Keyword Analysis', 'Content Optimization', 'Performance Analysis', 'Monthly Reports'],
            'category': 'marketing',
            'icon_name': 'seo',
            'is_featured': False,
            'is_active': True,
            'order': 1
        },
        {
            'title_ar': 'التسويق عبر البريد الإلكتروني',
            'title_en': 'Email Marketing',
            'description_ar': 'حملات تسويقية فعالة عبر البريد الإلكتروني',
            'description_en': 'Effective email marketing campaigns',
            'features_ar': ['قوائم بريدية', 'تصميم قوالب', 'تحليل النتائج', 'أتمتة الحملات'],
            'features_en': ['Mailing Lists', 'Template Design', 'Result Analysis', 'Campaign Automation'],
            'category': 'marketing',
            'icon_name': 'email',
            'is_featured': False,
            'is_active': True,
            'order': 2
        }
    ]
    
    # Create services
    created_services = []
    for service_data in sample_services:
        service = Service.objects.create(**service_data)
        created_services.append(service)
        print(f"Created service: {service.title_en}")
    
    print(f"\nSuccessfully created {len(created_services)} sample services!")
    print("\nYou can now view them at:")
    print("- Django Admin: http://127.0.0.1:8000/admin/content_management/service/")
    print("- React Page: http://localhost:5173/#/services")
    print("- API Endpoint: http://127.0.0.1:8000/api/services/")

if __name__ == "__main__":
    create_sample_services()
