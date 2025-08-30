#!/usr/bin/env python
"""
Script to publish blog posts
"""
import os
import django
from django.utils import timezone

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'takweensoft_backend.settings')
django.setup()

from content_management.models import BlogPost

def publish_blog_posts():
    """Publish blog posts"""
    
    print("🚀 Publishing blog posts...")
    print("=" * 50)
    
    # Get all draft posts
    draft_posts = BlogPost.objects.filter(status='draft')
    
    if not draft_posts.exists():
        print("✅ No draft posts found!")
        return
    
    print(f"📝 Found {draft_posts.count()} draft posts")
    
    for post in draft_posts:
        try:
            # Update status to published
            post.status = 'published'
            post.published_date = timezone.now()
            post.save()
            
            print(f"✅ Published: {post.title_ar}")
            print(f"   Slug: {post.slug}")
            print(f"   URL: /blog/{post.slug}")
            print("-" * 30)
            
        except Exception as e:
            print(f"❌ Error publishing {post.title_ar}: {e}")
    
    print("🎉 All posts published successfully!")

if __name__ == '__main__':
    publish_blog_posts()
