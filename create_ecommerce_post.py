#!/usr/bin/env python
"""
Script to create the e-commerce Saudi Arabia blog post
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'takweensoft_backend.settings')
django.setup()

from content_management.models import BlogPost
from django.utils.text import slugify

def create_ecommerce_post():
    """Create the e-commerce Saudi Arabia blog post"""
    
    # Check if post already exists
    existing_post = BlogPost.objects.filter(slug='e-commerce-saudi-arabia').first()
    if existing_post:
        print(f"✅ Post already exists with ID: {existing_post.id}")
        print(f"   Title: {existing_post.title_ar}")
        print(f"   Slug: {existing_post.slug}")
        print(f"   Status: {'Published' if existing_post.is_published else 'Draft'}")
        return existing_post
    
    # Create new post
    post_data = {
        'title_ar': 'التجارة الإلكترونية في السعودية: مستقبل التسوق الرقمي',
        'title_en': 'E-commerce in Saudi Arabia: The Future of Digital Shopping',
        'slug': 'e-commerce-saudi-arabia',
        'excerpt_ar': 'تعتبر التجارة الإلكترونية في السعودية من أسرع القطاعات نموا في المنطقة، مع تحول المستهلكين إلى التسوق الرقمي وزيادة الاعتماد على التكنولوجيا.',
        'excerpt_en': 'E-commerce in Saudi Arabia is considered one of the fastest-growing sectors in the region, with consumers shifting to digital shopping and increasing reliance on technology.',
        'content_ar': '''
# التجارة الإلكترونية في السعودية: مستقبل التسوق الرقمي

## مقدمة
تعتبر التجارة الإلكترونية في السعودية من أسرع القطاعات نمواً في المنطقة، حيث تشهد تطوراً متسارعاً مع تزايد اعتماد المستهلكين على التسوق الرقمي.

## النمو المتسارع
- نمو بنسبة 32% سنوياً
- حجم السوق يتجاوز 8 مليار دولار
- أكثر من 60% من السعوديين يتسوقون أونلاين

## العوامل المساعدة
1. **رؤية 2030**: دعم الحكومة للتحول الرقمي
2. **التكنولوجيا**: انتشار الهواتف الذكية والإنترنت
3. **الدفع الإلكتروني**: أنظمة دفع متطورة
4. **الخدمات اللوجستية**: شبكة توصيل متقدمة

## التحديات والحلول
### التحديات:
- الثقة في الأمان الإلكتروني
- جودة المنتجات
- خدمة العملاء

### الحلول:
- تشفير متقدم للمعاملات
- ضمان الجودة
- دعم عملاء 24/7

## مستقبل القطاع
- الذكاء الاصطناعي في التوصيات
- الواقع المعزز للمعاينة
- الدفع بالعملات الرقمية
- التسوق الصوتي

## الخلاصة
التجارة الإلكترونية في السعودية تشكل مستقبل التسوق، مع فرص هائلة للشركات والمطورين.
        ''',
        'content_en': '''
# E-commerce in Saudi Arabia: The Future of Digital Shopping

## Introduction
E-commerce in Saudi Arabia is one of the fastest-growing sectors in the region, experiencing rapid development as consumers increasingly rely on digital shopping.

## Rapid Growth
- 32% annual growth rate
- Market size exceeds $8 billion
- Over 60% of Saudis shop online

## Contributing Factors
1. **Vision 2030**: Government support for digital transformation
2. **Technology**: Widespread smartphone and internet adoption
3. **Digital Payments**: Advanced payment systems
4. **Logistics**: Advanced delivery network

## Challenges and Solutions
### Challenges:
- Trust in electronic security
- Product quality
- Customer service

### Solutions:
- Advanced transaction encryption
- Quality assurance
- 24/7 customer support

## Future of the Sector
- AI-powered recommendations
- AR for product preview
- Cryptocurrency payments
- Voice shopping

## Conclusion
E-commerce in Saudi Arabia represents the future of shopping, with tremendous opportunities for companies and developers.
        ''',
        'meta_description_ar': 'اكتشف مستقبل التجارة الإلكترونية في السعودية، النمو المتسارع، التحديات والحلول، والفرص المتاحة للشركات التقنية.',
        'meta_description_en': 'Discover the future of e-commerce in Saudi Arabia, rapid growth, challenges and solutions, and opportunities for technology companies.',
        'tags_ar': ['التسوق الرقمي', 'السعودية', 'التجارة الإلكترونية', 'رؤية 2030', 'التحول الرقمي'],
        'tags_en': ['Digital Shopping', 'Saudi Arabia', 'E-commerce', 'Vision 2030', 'Digital Transformation'],
        'category_ar': 'التجارة الإلكترونية',
        'category_en': 'E-commerce',
        'is_published': True,
        'featured': True
    }
    
    try:
        # Create the blog post
        post = BlogPost.objects.create(**post_data)
        print(f"✅ Created blog post successfully!")
        print(f"   ID: {post.id}")
        print(f"   Title: {post.title_ar}")
        print(f"   Slug: {post.slug}")
        print(f"   Status: {'Published' if post.is_published else 'Draft'}")
        print(f"   URL: /blog/{post.slug}")
        return post
        
    except Exception as e:
        print(f"❌ Error creating blog post: {e}")
        return None

if __name__ == '__main__':
    print("🚀 Creating e-commerce Saudi Arabia blog post...")
    create_ecommerce_post()
    print("✅ Done!")
