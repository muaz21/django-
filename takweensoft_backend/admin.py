from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from content_management.models import BlogPost, Hero, Portfolio, Service, Pricing

# Customize the admin site
admin.site.site_header = "Takween Soft Administration"
admin.site.site_title = "Takween Soft Admin Portal"
admin.site.index_title = "Welcome to Takween Soft Administration"

# Customize User Admin
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'date_joined')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('-date_joined',)
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

# Blog Post Admin
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'category', 'created_at', 'author')
    search_fields = ('title', 'content', 'author__username')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    
    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'content', 'excerpt', 'featured_image')
        }),
        ('Metadata', {
            'fields': ('author', 'category', 'tags', 'status')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

# Hero Admin
@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'is_active', 'order', 'created_at')
    list_filter = ('is_active', 'created_at')
    list_editable = ('is_active', 'order')
    search_fields = ('title', 'subtitle')
    
    fieldsets = (
        ('Content', {
            'fields': ('title', 'subtitle', 'description', 'background_image')
        }),
        ('Settings', {
            'fields': ('is_active', 'order', 'button_text', 'button_link')
        }),
    )

# Portfolio Admin
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'client', 'is_featured', 'created_at')
    list_filter = ('category', 'is_featured', 'created_at')
    list_editable = ('is_featured',)
    search_fields = ('title', 'description', 'client')
    prepopulated_fields = {'slug': ('title',)}
    
    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'description', 'featured_image')
        }),
        ('Details', {
            'fields': ('category', 'client', 'technologies', 'project_url')
        }),
        ('Settings', {
            'fields': ('is_featured', 'order')
        }),
    )

# Service Admin
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_active', 'order', 'created_at')
    list_filter = ('category', 'is_active', 'created_at')
    list_editable = ('is_active', 'order')
    search_fields = ('name', 'description')
    
    fieldsets = (
        ('Content', {
            'fields': ('name', 'description', 'icon', 'image')
        }),
        ('Settings', {
            'fields': ('category', 'is_active', 'order')
        }),
    )

# Pricing Admin
@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'currency', 'is_popular', 'is_active', 'created_at')
    list_filter = ('is_popular', 'is_active', 'currency', 'created_at')
    list_editable = ('is_popular', 'is_active')
    search_fields = ('name', 'description')
    
    fieldsets = (
        ('Content', {
            'fields': ('name', 'description', 'price', 'currency')
        }),
        ('Features', {
            'fields': ('features', 'highlighted_features')
        }),
        ('Settings', {
            'fields': ('is_popular', 'is_active', 'order')
        }),
    )

# Re-register User admin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Customize admin ordering
admin.site.enable_nav_sidebar = True
