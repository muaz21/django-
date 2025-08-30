#!/usr/bin/env python
"""
Script to check blog posts with detailed information
"""
import os
import django
from django.utils import timezone

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'takweensoft_backend.settings')
django.setup()

from content_management.models import BlogPost

def check_blog_posts_detailed():
    """Check current blog posts with detailed info"""
    
    print("🔍 Detailed Blog Posts Check:")
    print("=" * 50)
    
    # Check all posts
    all_posts = BlogPost.objects.all().order_by('-created_at')
    
    print(f"📊 Total Posts in Database: {all_posts.count()}")
    print(f"🕐 Current Time: {timezone.now()}")
    print("-" * 50)
    
    for post in all_posts:
        print(f"📝 Post ID: {post.id}")
        print(f"   Title: {post.title_en}")
        print(f"   Slug: {post.slug}")
        print(f"   Status: {post.status}")
        print(f"   Published Date: {post.published_date}")
        print(f"   Created: {post.created_at}")
        print(f"   Updated: {post.updated_at}")
        
        # Check if it meets API criteria
        is_published = post.status == 'published'
        has_published_date = post.published_date is not None
        is_past_date = has_published_date and post.published_date <= timezone.now()
        
        print(f"   ✅ Status Published: {is_published}")
        print(f"   ✅ Has Published Date: {has_published_date}")
        print(f"   ✅ Is Past Date: {is_past_date}")
        print(f"   🔗 Would Appear in API: {is_published and has_published_date and is_past_date}")
        print("-" * 30)
    
    # Check what would appear in API
    print("\n🔍 API Query Results:")
    print("=" * 50)
    
    api_posts = BlogPost.objects.filter(
        status='published', 
        published_date__lte=timezone.now()
    ).order_by('-published_date')
    
    print(f"📊 Posts that would appear in API: {api_posts.count()}")
    
    for post in api_posts:
        print(f"   ✅ {post.title_en} (ID: {post.id})")
    
    # Check posts that should appear but don't
    print("\n❌ Posts that should appear but don't:")
    print("=" * 50)
    
    should_appear = BlogPost.objects.filter(status='published')
    dont_appear = []
    
    for post in should_appear:
        if not post.published_date or post.published_date > timezone.now():
            dont_appear.append(post)
    
    if dont_appear:
        for post in dont_appear:
            print(f"   ❌ {post.title_en} (ID: {post.id})")
            print(f"      Status: {post.status}")
            print(f"      Published Date: {post.published_date}")
            if post.published_date:
                print(f"      Is Future: {post.published_date > timezone.now()}")
            else:
                print(f"      No Published Date")
    else:
        print("   ✅ All published posts have valid published dates")

if __name__ == '__main__':
    check_blog_posts_detailed()
