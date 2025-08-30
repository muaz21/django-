from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from .models import (
    HeroSection, PricingPackage, Service, Portfolio, 
    BlogPost, ContactSubmission, SiteSettings
)


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ['title_en', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title_ar', 'title_en', 'description_ar', 'description_en']
    fieldsets = (
        (_('Content'), {
            'fields': ('title_ar', 'title_en', 'subtitle_ar', 'subtitle_en', 
                      'description_ar', 'description_en')
        }),
        (_('Media'), {
            'fields': ('background_image',)
        }),
        (_('Call to Action'), {
            'fields': ('cta_text_ar', 'cta_text_en', 'cta_url')
        }),
        (_('Settings'), {
            'fields': ('is_active',)
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return ['created_at', 'updated_at']
        return []


@admin.register(PricingPackage)
class PricingPackageAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'price', 'currency', 'is_popular', 'is_active', 'order']
    list_filter = ['currency', 'is_popular', 'is_active']
    search_fields = ['name_ar', 'name_en', 'description_ar', 'description_en']
    list_editable = ['order', 'is_popular', 'is_active']
    ordering = ['order', 'price']
    
    fieldsets = (
        (_('Package Details'), {
            'fields': ('name_ar', 'name_en', 'description_ar', 'description_en')
        }),
        (_('Pricing'), {
            'fields': ('price', 'currency', 'period_ar', 'period_en')
        }),
        (_('Features'), {
            'fields': ('features_ar', 'features_en'),
            'description': _('Enter features as JSON array, e.g., ["Feature 1", "Feature 2"]')
        }),
        (_('Settings'), {
            'fields': ('is_popular', 'is_active', 'order')
        }),
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title_en', 'category', 'is_featured', 'is_active', 'order']
    list_filter = ['category', 'is_featured', 'is_active']
    search_fields = ['title_ar', 'title_en', 'description_ar', 'description_en']
    list_editable = ['order', 'is_featured', 'is_active']
    ordering = ['category', 'order']
    
    fieldsets = (
        (_('Service Details'), {
            'fields': ('title_ar', 'title_en', 'description_ar', 'description_en', 'category')
        }),
        (_('Features'), {
            'fields': ('features_ar', 'features_en'),
            'description': _('Enter features as JSON array, e.g., ["Feature 1", "Feature 2"]')
        }),
        (_('Display'), {
            'fields': ('icon_name', 'image')
        }),
        (_('Settings'), {
            'fields': ('is_featured', 'is_active', 'order')
        }),
    )


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title_en', 'category', 'completed_date', 'is_featured', 'is_active']
    list_filter = ['category', 'is_featured', 'is_active', 'completed_date']
    search_fields = ['title_ar', 'title_en', 'description_ar', 'description_en']
    list_editable = ['is_featured', 'is_active']
    date_hierarchy = 'completed_date'
    ordering = ['-completed_date', 'order']
    
    fieldsets = (
        (_('Project Details'), {
            'fields': ('title_ar', 'title_en', 'description_ar', 'description_en', 'category')
        }),
        (_('Project Challenge & Solution'), {
            'fields': ('client_challenge_ar', 'client_challenge_en', 
                      'solution_ar', 'solution_en')
        }),
        (_('Technical Details'), {
            'fields': ('features_ar', 'features_en', 'technologies'),
            'description': _('Enter as JSON arrays')
        }),
        (_('Links & Media'), {
            'fields': ('image', 'live_url', 'github_url')
        }),
        (_('Settings'), {
            'fields': ('is_featured', 'is_active', 'order', 'completed_date')
        }),
    )

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return '-'
    display_image.short_description = _('Image')


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title_en', 'status', 'is_featured', 'published_date', 'reading_time']
    list_filter = ['status', 'is_featured', 'published_date', 'category_en']
    search_fields = ['title_ar', 'title_en', 'excerpt_ar', 'excerpt_en', 'slug']
    list_editable = ['status', 'is_featured']
    prepopulated_fields = {'slug': ('title_en',)}
    date_hierarchy = 'published_date'
    ordering = ['-published_date', '-created_at']
    
    fieldsets = (
        (_('Post Details'), {
            'fields': ('title_ar', 'title_en', 'slug', 'author')
        }),
        (_('Content'), {
            'fields': ('excerpt_ar', 'excerpt_en', 'content_ar', 'content_en')
        }),
        (_('SEO & Meta'), {
            'fields': ('meta_description_ar', 'meta_description_en')
        }),
        (_('Categorization'), {
            'fields': ('category_ar', 'category_en', 'tags_ar', 'tags_en'),
            'description': _('Enter tags as JSON arrays')
        }),
        (_('Media & Settings'), {
            'fields': ('featured_image', 'reading_time', 'is_featured', 'status', 'published_date')
        }),
    )

    def save_model(self, request, obj, form, change):
        if obj.status == 'published' and not obj.published_date:
            from django.utils import timezone
            obj.published_date = timezone.now()
        super().save_model(request, obj, form, change)


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'service_type', 'is_read', 'created_at']
    list_filter = ['is_read', 'service_type', 'created_at']
    search_fields = ['name', 'email', 'message']
    list_editable = ['is_read']
    readonly_fields = ['name', 'email', 'phone', 'service_type', 'message', 'created_at']
    ordering = ['-created_at']
    
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return True


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Site Information'), {
            'fields': ('site_title_ar', 'site_title_en', 'site_description_ar', 'site_description_en')
        }),
        (_('Contact Information'), {
            'fields': ('contact_email', 'contact_phone')
        }),
        (_('Social Media'), {
            'fields': ('social_facebook', 'social_twitter', 'social_instagram', 'social_linkedin')
        }),
        (_('Media'), {
            'fields': ('logo', 'favicon')
        }),
    )

    def has_add_permission(self, request):
        # Only allow one instance
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


# Customize admin site
admin.site.site_header = "Takween Soft Content Management"
admin.site.site_title = "Takween Soft CMS"
admin.site.index_title = "Content Management Dashboard"
