#!/usr/bin/env python
"""
Script to create sample blog data for the Takween Soft website
"""
import os
import sys
import django
from datetime import datetime, date

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'takweensoft_backend.settings')
django.setup()

from content_management.models import BlogPost

def create_blog_data():
    """Create sample blog posts"""
    
    # Clear existing data
    BlogPost.objects.all().delete()
    
    # Create blog posts
    posts = [
        {
            'title_ar': 'دليل التجارة الإلكترونية للسوق السعودي واليمني',
            'title_en': 'E-commerce Guide for Saudi and Yemeni Markets',
            'slug': 'ecommerce-guide-saudi-yemen',
            'excerpt_ar': 'دليل شامل لبناء متجر إلكتروني ناجح في السوق السعودي واليمني مع نصائح حول الدفع والشحن',
            'excerpt_en': 'Comprehensive guide to building a successful e-commerce store in Saudi and Yemeni markets with payment and shipping tips',
            'content_ar': '''يشهد قطاع التجارة الإلكترونية نمواً متسارعاً في المنطقة العربية، خاصة في السعودية واليمن. يتطلب النجاح في هذا المجال فهماً عميقاً للثقافة المحلية واحتياجات العملاء.

أهم العوامل للنجاح:
1. تصميم واجهة مستخدم تدعم اللغة العربية
2. تكامل أنظمة الدفع المحلية
3. حلول الشحن المناسبة للمنطقة
4. خدمة عملاء باللغة العربية

التحديات الرئيسية:
- البنية التحتية للإنترنت
- طرق الدفع التقليدية
- الثقة في التسوق الإلكتروني

الحلول:
- استخدام تقنيات حديثة لتحسين الأداء
- تقديم خيارات دفع متنوعة
- بناء الثقة من خلال التقييمات والضمانات''',
            'content_en': '''E-commerce is experiencing rapid growth in the Arab region, especially in Saudi Arabia and Yemen. Success in this field requires deep understanding of local culture and customer needs.

Key Success Factors:
1. User interface design supporting Arabic language
2. Integration of local payment systems  
3. Appropriate shipping solutions for the region
4. Arabic customer service

Main Challenges:
- Internet infrastructure
- Traditional payment methods
- Trust in online shopping

Solutions:
- Using modern technologies to improve performance
- Providing diverse payment options
- Building trust through reviews and guarantees''',
            'meta_description_ar': 'دليل شامل للتجارة الإلكترونية في السعودية واليمن يتضمن نصائح للدفع والشحن وبناء الثقة',
            'meta_description_en': 'Comprehensive e-commerce guide for Saudi Arabia and Yemen including payment, shipping and trust-building tips',
            'tags_ar': ['التجارة الإلكترونية', 'السعودية', 'اليمن', 'الدفع الإلكتروني'],
            'tags_en': ['E-commerce', 'Saudi Arabia', 'Yemen', 'Electronic Payment'],
            'category_ar': 'التجارة الإلكترونية',
            'category_en': 'E-commerce',
            'author': 'Takweensoft Team',
            'reading_time': 8,
            'is_featured': True,
            'status': 'published',
            'published_date': datetime(2024, 3, 20, 10, 0, 0)
        },
        {
            'title_ar': 'رؤية 2030 والتحول الرقمي في السعودية',
            'title_en': 'Vision 2030 and Digital Transformation in Saudi Arabia',
            'slug': 'vision-2030-digital-transformation',
            'excerpt_ar': 'كيف تساهم رؤية السعودية 2030 في تسريع التحول الرقمي وما هي الفرص المتاحة للشركات التقنية',
            'excerpt_en': 'How Saudi Vision 2030 accelerates digital transformation and opportunities available for tech companies',
            'content_ar': '''تمثل رؤية السعودية 2030 نقطة تحول مهمة في مسيرة التنمية الاقتصادية، حيث تركز على التحول الرقمي كأحد المحاور الأساسية.

المبادرات الرئيسية:
1. برنامج التحول الوطني
2. مبادرة الحكومة الرقمية
3. مدينة نيوم الذكية
4. صندوق الاستثمارات العامة

الفرص للشركات:
- الاستثمار في التقنيات الناشئة
- تطوير الحلول الذكية للمدن
- التعليم الرقمي والتدريب
- الصحة الرقمية

التحديات:
- نقص المواهب التقنية
- الحاجة لتطوير البنية التحتية
- مقاومة التغيير

النتائج المتوقعة:
- اقتصاد معرفي متطور
- مجتمع رقمي متقدم
- حكومة فعالة ومرنة''',
            'content_en': '''Saudi Vision 2030 represents an important turning point in economic development, focusing on digital transformation as one of the main pillars.

Key Initiatives:
1. National Transformation Program
2. Digital Government Initiative  
3. NEOM Smart City
4. Public Investment Fund

Opportunities for Companies:
- Investment in emerging technologies
- Development of smart city solutions
- Digital education and training
- Digital health

Challenges:
- Shortage of technical talent
- Need for infrastructure development
- Resistance to change

Expected Results:
- Advanced knowledge economy
- Advanced digital society
- Efficient and flexible government''',
            'meta_description_ar': 'تأثير رؤية 2030 على التحول الرقمي في السعودية والفرص المتاحة للشركات التقنية',
            'meta_description_en': 'Impact of Vision 2030 on digital transformation in Saudi Arabia and opportunities for tech companies',
            'tags_ar': ['رؤية 2030', 'التحول الرقمي', 'السعودية', 'نيوم'],
            'tags_en': ['Vision 2030', 'Digital Transformation', 'Saudi Arabia', 'NEOM'],
            'category_ar': 'التحول الرقمي',
            'category_en': 'Digital Transformation',
            'author': 'Takweensoft Team',
            'reading_time': 10,
            'is_featured': True,
            'status': 'published',
            'published_date': datetime(2024, 3, 18, 14, 30, 0)
        },
        {
            'title_ar': 'الذكاء الاصطناعي وتطبيقاته في الأعمال',
            'title_en': 'Artificial Intelligence and Its Business Applications',
            'slug': 'artificial-intelligence-business-applications',
            'excerpt_ar': 'كيف يمكن للشركات الاستفادة من تقنيات الذكاء الاصطناعي لتحسين العمليات وزيادة الكفاءة',
            'excerpt_en': 'How companies can leverage AI technologies to improve operations and increase efficiency',
            'content_ar': '''يمثل الذكاء الاصطناعي ثورة حقيقية في عالم الأعمال، حيث يمكنه تحويل طريقة عمل الشركات وتفاعلها مع العملاء.

تطبيقات الذكاء الاصطناعي:
1. خدمة العملاء الآلية (Chatbots)
2. تحليل البيانات والتنبؤات
3. أتمتة العمليات
4. التسويق المخصص

الفوائد:
- تحسين تجربة العملاء
- زيادة الكفاءة التشغيلية
- تقليل التكاليف
- اتخاذ قرارات مدروسة

التحديات:
- الاستثمار الأولي المرتفع
- الحاجة لتدريب الموظفين
- قضايا الخصوصية والأمان

نصائح للتطبيق:
- البدء بمشاريع صغيرة
- التركيز على ROI
- الاستثمار في التدريب
- وضع استراتيجية واضحة''',
            'content_en': '''Artificial Intelligence represents a real revolution in the business world, transforming how companies operate and interact with customers.

AI Applications:
1. Automated Customer Service (Chatbots)
2. Data Analysis and Predictions
3. Process Automation
4. Personalized Marketing

Benefits:
- Improved customer experience
- Increased operational efficiency
- Cost reduction
- Informed decision making

Challenges:
- High initial investment
- Need for employee training
- Privacy and security issues

Implementation Tips:
- Start with small projects
- Focus on ROI
- Invest in training
- Develop clear strategy''',
            'meta_description_ar': 'دليل شامل لتطبيقات الذكاء الاصطناعي في الأعمال وكيفية الاستفادة منها لتحسين الكفاءة',
            'meta_description_en': 'Comprehensive guide to AI applications in business and how to leverage them for improved efficiency',
            'tags_ar': ['الذكاء الاصطناعي', 'التقنية', 'الأعمال', 'الأتمتة'],
            'tags_en': ['Artificial Intelligence', 'Technology', 'Business', 'Automation'],
            'category_ar': 'التقنية',
            'category_en': 'Technology',
            'author': 'Takweensoft Team',
            'reading_time': 7,
            'is_featured': False,
            'status': 'published',
            'published_date': datetime(2024, 3, 8, 9, 15, 0)
        }
    ]
    
    for post_data in posts:
        BlogPost.objects.create(**post_data)
    
    print(f"✅ Created {len(posts)} blog posts")

if __name__ == '__main__':
    print("🚀 Creating sample blog data for Takween Soft website...")
    
    create_blog_data()
    
    print("✅ Blog data created successfully!")
    print("\n🎯 You can now:")
    print("1. Visit: http://127.0.0.1:8000/admin/content_management/blogpost/")
    print("2. Check API: http://127.0.0.1:8000/api/blog/")
    print("3. View your React blog page: http://localhost:5173/#/blog")
