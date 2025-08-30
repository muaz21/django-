from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    HeroSectionViewSet, PricingPackageViewSet, ServiceViewSet,
    PortfolioViewSet, BlogPostViewSet, ContactSubmissionViewSet,
    SiteSettingsViewSet
)

# Create router and register viewsets
router = DefaultRouter()
router.register(r'hero', HeroSectionViewSet, basename='hero')
router.register(r'pricing', PricingPackageViewSet, basename='pricing')
router.register(r'services', ServiceViewSet, basename='services')
router.register(r'portfolio', PortfolioViewSet, basename='portfolio')
router.register(r'blog', BlogPostViewSet, basename='blog')
router.register(r'contact', ContactSubmissionViewSet, basename='contact')
router.register(r'settings', SiteSettingsViewSet, basename='settings')

urlpatterns = [
    path('', include(router.urls)),
]

# API endpoints will be available at:
# /api/hero/ - Hero sections
# /api/hero/active/ - Active hero section
# /api/pricing/ - Pricing packages
# /api/pricing/featured/ - Featured pricing packages
# /api/services/ - Services
# /api/services/by_category/ - Services grouped by category
# /api/services/featured/ - Featured services
# /api/portfolio/ - Portfolio projects
# /api/portfolio/by_category/ - Portfolio grouped by category
# /api/portfolio/featured/ - Featured portfolio projects
# /api/portfolio/recent/ - Recent portfolio projects
# /api/blog/ - Blog posts
# /api/blog/{slug}/ - Individual blog post
# /api/blog/featured/ - Featured blog posts
# /api/blog/recent/ - Recent blog posts
# /api/blog/categories/ - Blog categories
# /api/contact/ - Contact form submissions (POST only)
# /api/settings/ - Site settings
# /api/settings/current/ - Current site settings
