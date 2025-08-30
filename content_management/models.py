from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator


class HeroSection(models.Model):
    """Hero section content model"""
    title_ar = models.CharField(_('Title (Arabic)'), max_length=200)
    title_en = models.CharField(_('Title (English)'), max_length=200)
    subtitle_ar = models.CharField(_('Subtitle (Arabic)'), max_length=200)
    subtitle_en = models.CharField(_('Subtitle (English)'), max_length=200)
    description_ar = models.TextField(_('Description (Arabic)'))
    description_en = models.TextField(_('Description (English)'))
    background_image = models.ImageField(_('Background Image'), upload_to='hero/')
    cta_text_ar = models.CharField(_('CTA Text (Arabic)'), max_length=100)
    cta_text_en = models.CharField(_('CTA Text (English)'), max_length=100)
    cta_url = models.URLField(_('CTA URL'), default='/contact')
    is_active = models.BooleanField(_('Is Active'), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Hero Section')
        verbose_name_plural = _('Hero Sections')
        ordering = ['-created_at']

    def __str__(self):
        return f"Hero: {self.title_en}"


class PricingPackage(models.Model):
    """Pricing package model"""
    CURRENCY_CHOICES = [
        ('SAR', 'Saudi Riyal'),
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
    ]
    
    name_ar = models.CharField(_('Package Name (Arabic)'), max_length=100)
    name_en = models.CharField(_('Package Name (English)'), max_length=100)
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2)
    currency = models.CharField(_('Currency'), max_length=3, choices=CURRENCY_CHOICES, default='SAR')
    period_ar = models.CharField(_('Period (Arabic)'), max_length=50, default='شهرياً')
    period_en = models.CharField(_('Period (English)'), max_length=50, default='monthly')
    description_ar = models.TextField(_('Description (Arabic)'))
    description_en = models.TextField(_('Description (English)'))
    features_ar = models.JSONField(_('Features (Arabic)'), default=list)
    features_en = models.JSONField(_('Features (English)'), default=list)
    is_popular = models.BooleanField(_('Is Popular'), default=False)
    is_active = models.BooleanField(_('Is Active'), default=True)
    order = models.PositiveIntegerField(_('Display Order'), default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Pricing Package')
        verbose_name_plural = _('Pricing Packages')
        ordering = ['order', 'price']

    def __str__(self):
        return f"{self.name_en} - {self.price} {self.currency}"


class Service(models.Model):
    """Service model"""
    SERVICE_CATEGORIES = [
        ('design', 'Design Services'),
        ('development', 'Development Services'),
        ('marketing', 'Marketing Services'),
        ('consulting', 'Consulting Services'),
    ]
    
    title_ar = models.CharField(_('Service Title (Arabic)'), max_length=200)
    title_en = models.CharField(_('Service Title (English)'), max_length=200)
    description_ar = models.TextField(_('Description (Arabic)'))
    description_en = models.TextField(_('Description (English)'))
    features_ar = models.JSONField(_('Features (Arabic)'), default=list)
    features_en = models.JSONField(_('Features (English)'), default=list)
    category = models.CharField(_('Category'), max_length=20, choices=SERVICE_CATEGORIES)
    icon_name = models.CharField(_('Icon Name'), max_length=50, help_text=_('Icon component name'))
    image = models.ImageField(_('Service Image'), upload_to='services/', blank=True, null=True)
    is_featured = models.BooleanField(_('Is Featured'), default=False)
    is_active = models.BooleanField(_('Is Active'), default=True)
    order = models.PositiveIntegerField(_('Display Order'), default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')
        ordering = ['category', 'order', 'title_en']

    def __str__(self):
        return f"{self.title_en} ({self.get_category_display()})"


class Portfolio(models.Model):
    """Portfolio project model"""
    PROJECT_CATEGORIES = [
        ('website', 'Website'),
        ('ecommerce', 'E-commerce'),
        ('mobile', 'Mobile App'),
        ('webapp', 'Web Application'),
        ('system', 'System/Software'),
    ]
    
    title_ar = models.CharField(_('Project Title (Arabic)'), max_length=200)
    title_en = models.CharField(_('Project Title (English)'), max_length=200)
    description_ar = models.TextField(_('Description (Arabic)'))
    description_en = models.TextField(_('Description (English)'))
    client_challenge_ar = models.TextField(_('Client Challenge (Arabic)'))
    client_challenge_en = models.TextField(_('Client Challenge (English)'))
    solution_ar = models.TextField(_('Solution (Arabic)'))
    solution_en = models.TextField(_('Solution (English)'))
    features_ar = models.JSONField(_('Features (Arabic)'), default=list)
    features_en = models.JSONField(_('Features (English)'), default=list)
    technologies = models.JSONField(_('Technologies'), default=list, help_text=_('List of technologies used'))
    category = models.CharField(_('Category'), max_length=20, choices=PROJECT_CATEGORIES)
    image = models.ImageField(_('Project Image'), upload_to='portfolio/')
    live_url = models.URLField(_('Live URL'), blank=True, null=True)
    github_url = models.URLField(_('GitHub URL'), blank=True, null=True)
    is_featured = models.BooleanField(_('Is Featured'), default=False)
    is_active = models.BooleanField(_('Is Active'), default=True)
    order = models.PositiveIntegerField(_('Display Order'), default=0)
    completed_date = models.DateField(_('Completion Date'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Portfolio Project')
        verbose_name_plural = _('Portfolio Projects')
        ordering = ['-completed_date', 'order']

    def __str__(self):
        return f"{self.title_en} ({self.get_category_display()})"


class BlogPost(models.Model):
    """Blog post model"""
    POST_STATUS = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]
    
    title_ar = models.CharField(_('Title (Arabic)'), max_length=200)
    title_en = models.CharField(_('Title (English)'), max_length=200)
    slug = models.SlugField(_('Slug'), unique=True, max_length=200)
    excerpt_ar = models.TextField(_('Excerpt (Arabic)'), max_length=500)
    excerpt_en = models.TextField(_('Excerpt (English)'), max_length=500)
    content_ar = models.TextField(_('Content (Arabic)'))
    content_en = models.TextField(_('Content (English)'))
    meta_description_ar = models.CharField(_('Meta Description (Arabic)'), max_length=160)
    meta_description_en = models.CharField(_('Meta Description (English)'), max_length=160)
    featured_image = models.ImageField(_('Featured Image'), upload_to='blog/')
    tags_ar = models.JSONField(_('Tags (Arabic)'), default=list)
    tags_en = models.JSONField(_('Tags (English)'), default=list)
    category_ar = models.CharField(_('Category (Arabic)'), max_length=100)
    category_en = models.CharField(_('Category (English)'), max_length=100)
    author = models.CharField(_('Author'), max_length=100, default='Takweensoft Team')
    reading_time = models.PositiveIntegerField(
        _('Reading Time (minutes)'), 
        validators=[MinValueValidator(1), MaxValueValidator(60)],
        default=5
    )
    is_featured = models.BooleanField(_('Is Featured'), default=False)
    status = models.CharField(_('Status'), max_length=10, choices=POST_STATUS, default='draft')
    published_date = models.DateTimeField(_('Published Date'), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Blog Post')
        verbose_name_plural = _('Blog Posts')
        ordering = ['-published_date', '-created_at']

    def __str__(self):
        return f"{self.title_en} ({self.status})"


class ContactSubmission(models.Model):
    """Contact form submission model"""
    name = models.CharField(_('Name'), max_length=100)
    email = models.EmailField(_('Email'))
    phone = models.CharField(_('Phone'), max_length=20, blank=True)
    service_type = models.CharField(_('Service Type'), max_length=100, blank=True)
    message = models.TextField(_('Message'))
    is_read = models.BooleanField(_('Is Read'), default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Contact Submission')
        verbose_name_plural = _('Contact Submissions')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.email}"


class SiteSettings(models.Model):
    """Global site settings model"""
    site_title_ar = models.CharField(_('Site Title (Arabic)'), max_length=200, default='تكوين سوفت')
    site_title_en = models.CharField(_('Site Title (English)'), max_length=200, default='Takween Soft')
    site_description_ar = models.TextField(_('Site Description (Arabic)'))
    site_description_en = models.TextField(_('Site Description (English)'))
    contact_email = models.EmailField(_('Contact Email'))
    contact_phone = models.CharField(_('Contact Phone'), max_length=20)
    social_facebook = models.URLField(_('Facebook URL'), blank=True)
    social_twitter = models.URLField(_('Twitter URL'), blank=True)
    social_instagram = models.URLField(_('Instagram URL'), blank=True)
    social_linkedin = models.URLField(_('LinkedIn URL'), blank=True)
    logo = models.ImageField(_('Logo'), upload_to='site/', blank=True, null=True)
    favicon = models.ImageField(_('Favicon'), upload_to='site/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Site Settings')
        verbose_name_plural = _('Site Settings')

    def __str__(self):
        return f"Site Settings - {self.site_title_en}"

    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        if not self.pk and SiteSettings.objects.exists():
            raise ValueError('Only one SiteSettings instance is allowed')
        super().save(*args, **kwargs)
