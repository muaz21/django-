#!/usr/bin/env python
"""
Script to create pricing package data for the Takween Soft website
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'takweensoft_backend.settings')
django.setup()

from content_management.models import PricingPackage

def create_pricing_data():
    """Create pricing packages"""
    
    # Clear existing data
    PricingPackage.objects.all().delete()
    
    # Create pricing packages
    packages = [
        {
            'name_ar': 'الباقة الأساسية',
            'name_en': 'Basic Package',
            'price': 2999.00,
            'currency': 'SAR',
            'period_ar': 'شهرياً',
            'period_en': 'monthly',
            'description_ar': 'مثالية للمشاريع الصغيرة والشركات الناشئة',
            'description_en': 'Ideal for small projects and startups',
            'features_ar': [
                'موقع إلكتروني احترافي',
                'تصميم متجاوب',
                'دومين مجاني لسنة',
                'استضافة لسنة',
                'دعم فني لـ 3 أشهر'
            ],
            'features_en': [
                'Professional website',
                'Responsive design',
                'Free domain for a year',
                'Annual hosting',
                '3 months technical support'
            ],
            'is_popular': False,
            'is_active': True,
            'order': 1
        },
        {
            'name_ar': 'الباقة الاحترافية',
            'name_en': 'Professional Package',
            'price': 5999.00,
            'currency': 'SAR',
            'period_ar': 'شهرياً',
            'period_en': 'monthly',
            'description_ar': 'الأفضل للشركات المتوسطة والمشاريع المتقدمة',
            'description_en': 'Best for medium companies and advanced projects',
            'features_ar': [
                'كل ما في الباقة الأساسية',
                'متجر إلكتروني متكامل',
                'نظام إدارة المحتوى',
                'تكامل مع وسائل الدفع',
                'دعم فني لـ 6 أشهر',
                'تحسين محركات البحث SEO'
            ],
            'features_en': [
                'Everything in Basic Package',
                'Complete e-commerce store',
                'Content management system',
                'Payment gateway integration',
                '6 months technical support',
                'SEO optimization'
            ],
            'is_popular': True,  # Most popular package
            'is_active': True,
            'order': 2
        },
        {
            'name_ar': 'الباقة المؤسسية',
            'name_en': 'Enterprise Package',
            'price': 9999.00,
            'currency': 'SAR',
            'period_ar': 'شهرياً',
            'period_en': 'monthly',
            'description_ar': 'للمؤسسات الكبيرة والمشاريع المعقدة',
            'description_en': 'For large enterprises and complex projects',
            'features_ar': [
                'كل ما في الباقة الاحترافية',
                'تطبيق جوال iOS & Android',
                'نظام إدارة متقدم',
                'تكامل مع الأنظمة الخارجية',
                'دعم فني على مدار الساعة',
                'تدريب الموظفين',
                'ضمان لمدة سنة'
            ],
            'features_en': [
                'Everything in Professional Package',
                'Mobile app iOS & Android',
                'Advanced management system',
                'Third-party integrations',
                '24/7 technical support',
                'Staff training',
                'One year warranty'
            ],
            'is_popular': False,
            'is_active': True,
            'order': 3
        }
    ]
    
    for package_data in packages:
        PricingPackage.objects.create(**package_data)
    
    print(f"✅ Created {len(packages)} pricing packages")

if __name__ == '__main__':
    print("🚀 Creating pricing data for Takween Soft website...")
    
    create_pricing_data()
    
    print("✅ Pricing data created successfully!")
    print("\n🎯 You can now:")
    print("1. Visit: http://127.0.0.1:8000/admin/content_management/pricingpackage/")
    print("2. Check API: http://127.0.0.1:8000/api/pricing/")
    print("3. View your React pricing section")
    print("\n💡 Update prices in Django Admin and see changes in real-time!")
