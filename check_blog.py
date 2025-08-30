#!/usr/bin/env python
"""
Script to check blog posts in Django
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'takweensoft_backend.settings')
django.setup()

from content_management.models import BlogPost

def check_blog_posts():
    """Check current blog posts"""
    
    print("🔍 Current Blog Posts in Django:")
    print("=" * 50)
    
    posts = BlogPost.objects.all().order_by('-created_at')
    
    if not posts.exists():
        print("❌ No blog posts found!")
        return
    
    # Get the first post to check available fields
    first_post = posts.first()
    print(f"📋 Available fields in BlogPost model:")
    for field in first_post._meta.fields:
        print(f"   - {field.name}: {field.get_internal_type()}")
    print("-" * 30)
    
    for post in posts:
        print(f"📝 Post ID: {post.id}")
        print(f"   Title (AR): {post.title_ar}")
        print(f"   Title (EN): {post.title_en}")
        print(f"   Slug: {post.slug}")
        print(f"   Status: {getattr(post, 'status', 'N/A')}")
        print(f"   Created: {post.created_at}")
        print(f"   Updated: {post.updated_at}")
        if hasattr(post, 'featured_image') and post.featured_image:
            print(f"   Featured Image: {post.featured_image.url}")
        else:
            print(f"   Featured Image: None")
        print("-" * 30)
    
    print(f"\n📊 Total Posts: {posts.count()}")
    
    # Count by status
    status_counts = {}
    for post in posts:
        status = getattr(post, 'status', 'unknown')
        status_counts[status] = status_counts.get(status, 0) + 1
    
    for status, count in status_counts.items():
        print(f"📊 {status}: {count}")

if __name__ == '__main__':
    check_blog_posts()
