#!/usr/bin/env python
"""
Script to update portfolio data to match React i18n data
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'takweensoft_backend.settings')
django.setup()

from content_management.models import Portfolio
from datetime import date

def update_portfolio_data():
    """Update portfolio projects to match React data"""
    
    # Clear existing data
    Portfolio.objects.all().delete()
    
    # Create portfolio projects matching React data
    projects = [
        {
            'title_ar': 'Datxsci.com',
            'title_en': 'Datxsci.com',
            'description_ar': 'منصة تقنية متقدمة لعلوم البيانات والذكاء الاصطناعي',
            'description_en': 'Advanced technology platform for data science and artificial intelligence',
            'client_challenge_ar': 'تطوير منصة متقدمة لعلوم البيانات مع واجهة مستخدم سهلة الاستخدام',
            'client_challenge_en': 'Develop advanced data science platform with user-friendly interface',
            'solution_ar': 'تصميم وتطوير منصة شاملة مع واجهة مستخدم عربية متطورة وأدوات تحليل متقدمة',
            'solution_en': 'Design and develop comprehensive platform with advanced Arabic UI and analysis tools',
            'features_ar': ['تحليل البيانات', 'التعلم الآلي', 'التقارير التفاعلية', 'واجهة عربية'],
            'features_en': ['Data Analysis', 'Machine Learning', 'Interactive Reports', 'Arabic Interface'],
            'technologies': ['Vue.js', 'Node.js', 'AI/ML', 'Data Science'],
            'category': 'website',
            'live_url': 'https://datxsci.com',
            'is_featured': True,
            'is_active': True,
            'order': 1,
            'completed_date': date(2024, 1, 15)
        },
        {
            'title_ar': 'Eplatx.com',
            'title_en': 'Eplatx.com',
            'description_ar': 'منصة حديثة ومتطورة للحلول التجارية الإلكترونية',
            'description_en': 'Modern and advanced platform for e-commerce business solutions',
            'client_challenge_ar': 'إنشاء منصة تجارة إلكترونية متكاملة مع أنظمة دفع آمنة',
            'client_challenge_en': 'Create integrated e-commerce platform with secure payment systems',
            'solution_ar': 'تطوير منصة تجارة إلكترونية كاملة مع نظام إدارة المخزون وأنظمة دفع متعددة',
            'solution_en': 'Develop complete e-commerce platform with inventory management and multiple payment systems',
            'features_ar': ['إدارة المنتجات', 'أنظمة الدفع', 'إدارة الطلبات', 'التقارير المالية'],
            'features_en': ['Product Management', 'Payment Systems', 'Order Management', 'Financial Reports'],
            'technologies': ['React.js', 'E-commerce', 'Payment Systems', 'Cloud'],
            'category': 'ecommerce',
            'live_url': 'https://eplatx.com',
            'is_featured': True,
            'is_active': True,
            'order': 2,
            'completed_date': date(2024, 2, 20)
        },
        {
            'title_ar': 'Aljassem BBB',
            'title_en': 'Aljassem BBB',
            'description_ar': 'موقع إلكتروني احترافي للأعمال التجارية والخدمات المؤسسية',
            'description_en': 'Professional website for business and institutional services',
            'client_challenge_ar': 'تطوير موقع احترافي يعكس هوية الشركة ويحسن الحضور الرقمي',
            'client_challenge_en': 'Develop professional website that reflects company identity and improves digital presence',
            'solution_ar': 'تصميم موقع احترافي متجاوب مع تحسين محركات البحث وواجهة مستخدم عصرية',
            'solution_en': 'Design responsive professional website with SEO optimization and modern user interface',
            'features_ar': ['تصميم متجاوب', 'تحسين SEO', 'إدارة المحتوى', 'التواصل مع العملاء'],
            'features_en': ['Responsive Design', 'SEO Optimization', 'Content Management', 'Customer Communication'],
            'technologies': ['Vue.js', 'Responsive Design', 'Business Solutions', 'SEO'],
            'category': 'website',
            'live_url': 'https://aljassemsbb.com',
            'is_featured': False,
            'is_active': True,
            'order': 3,
            'completed_date': date(2023, 12, 10)
        },
        {
            'title_ar': 'Salasah.sa',
            'title_en': 'Salasah.sa',
            'description_ar': 'منصة سعودية متطورة تقدم حلول رقمية مبتكرة',
            'description_en': 'Advanced Saudi platform providing innovative digital solutions',
            'client_challenge_ar': 'إنشاء منصة رقمية سعودية تلبي احتياجات السوق المحلي',
            'client_challenge_en': 'Create Saudi digital platform that meets local market needs',
            'solution_ar': 'تطوير منصة شاملة مع واجهة عربية محلية وحلول تقنية متطورة',
            'solution_en': 'Develop comprehensive platform with localized Arabic interface and advanced technical solutions',
            'features_ar': ['حلول محلية', 'واجهة عربية', 'تطبيق الجوال', 'دعم فني'],
            'features_en': ['Local Solutions', 'Arabic Interface', 'Mobile App', 'Technical Support'],
            'technologies': ['React.js', 'Arabic UI/UX', 'Saudi Market', 'Mobile-First'],
            'category': 'website',
            'live_url': 'https://salasah.sa',
            'is_featured': True,
            'is_active': True,
            'order': 4,
            'completed_date': date(2024, 3, 25)
        },
        {
            'title_ar': 'موقع تكوين سوفت',
            'title_en': 'Takween Soft Website',
            'description_ar': 'موقع الشركة الرسمي المطور بأحدث التقنيات مع تصميم متجاوب وأداء عالي',
            'description_en': 'Official company website built with cutting-edge technologies featuring responsive design and high performance',
            'client_challenge_ar': 'تطوير موقع شركة حديث يعكس الهوية التقنية المتطورة للشركة',
            'client_challenge_en': 'Developing a modern company website that reflects the advanced technical identity of the company',
            'solution_ar': 'تصميم وتطوير موقع متطور باستخدام React وVite مع تجربة مستخدم استثنائية',
            'solution_en': 'Design and development of an advanced website using React and Vite with exceptional user experience',
            'features_ar': ['React 18', 'Vite', 'تصميم متجاوب', 'تحسين SEO', 'أداء عالي', 'واجهة ثنائية اللغة'],
            'features_en': ['React 18', 'Vite', 'Responsive Design', 'SEO Optimization', 'High Performance', 'Bilingual Interface'],
            'technologies': ['React 18', 'Vite', 'Tailwind CSS', 'i18n', 'AOS'],
            'category': 'website',
            'live_url': 'https://takweensoft.com',
            'is_featured': True,
            'is_active': True,
            'order': 5,
            'completed_date': date(2024, 4, 10)
        }
    ]
    
    for project_data in projects:
        Portfolio.objects.create(**project_data)
    
    print(f"✅ Updated {len(projects)} portfolio projects to match React data")

if __name__ == '__main__':
    print("🔄 Updating portfolio data to match React i18n...")
    update_portfolio_data()
    print("✅ Portfolio data updated successfully!")
    print("\n🎯 Projects now match React data structure!")
    print("📱 Test: http://localhost:5173/#/portfolio")
    print("🔧 Admin: http://127.0.0.1:8000/admin/content_management/portfolio/")
