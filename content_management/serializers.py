from rest_framework import serializers
from .models import (
    HeroSection, PricingPackage, Service, Portfolio, 
    BlogPost, ContactSubmission, SiteSettings
)


class HeroSectionSerializer(serializers.ModelSerializer):
    background_image_url = serializers.SerializerMethodField()

    class Meta:
        model = HeroSection
        fields = [
            'id', 'title_ar', 'title_en', 'subtitle_ar', 'subtitle_en',
            'description_ar', 'description_en', 'background_image', 
            'background_image_url', 'cta_text_ar', 'cta_text_en', 'cta_url',
            'is_active', 'created_at', 'updated_at'
        ]

    def get_background_image_url(self, obj):
        if obj.background_image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.background_image.url)
            return obj.background_image.url
        return None


class PricingPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingPackage
        fields = [
            'id', 'name_ar', 'name_en', 'price', 'currency', 'period_ar', 'period_en',
            'description_ar', 'description_en', 'features_ar', 'features_en',
            'is_popular', 'is_active', 'order', 'created_at', 'updated_at'
        ]


class ServiceSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    category_display = serializers.CharField(source='get_category_display', read_only=True)

    class Meta:
        model = Service
        fields = [
            'id', 'title_ar', 'title_en', 'description_ar', 'description_en',
            'features_ar', 'features_en', 'category', 'category_display',
            'icon_name', 'image', 'image_url', 'is_featured', 'is_active',
            'order', 'created_at', 'updated_at'
        ]

    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None


class PortfolioSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    category_display = serializers.CharField(source='get_category_display', read_only=True)

    class Meta:
        model = Portfolio
        fields = [
            'id', 'title_ar', 'title_en', 'description_ar', 'description_en',
            'client_challenge_ar', 'client_challenge_en', 'solution_ar', 'solution_en',
            'features_ar', 'features_en', 'technologies', 'category', 'category_display',
            'image', 'image_url', 'live_url', 'github_url', 'is_featured', 'is_active',
            'order', 'completed_date', 'created_at', 'updated_at'
        ]

    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None


class BlogPostSerializer(serializers.ModelSerializer):
    featured_image_url = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = [
            'id', 'title_ar', 'title_en', 'slug', 'excerpt_ar', 'excerpt_en',
            'content_ar', 'content_en', 'meta_description_ar', 'meta_description_en',
            'featured_image', 'featured_image_url', 'tags_ar', 'tags_en',
            'category_ar', 'category_en', 'author', 'reading_time', 'is_featured',
            'status', 'published_date', 'created_at', 'updated_at'
        ]

    def get_featured_image_url(self, obj):
        if obj.featured_image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.featured_image.url)
            return obj.featured_image.url
        return None


class BlogPostListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for blog post lists"""
    featured_image_url = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = [
            'id', 'title_ar', 'title_en', 'slug', 'excerpt_ar', 'excerpt_en',
            'featured_image_url', 'tags_ar', 'tags_en', 'category_ar', 'category_en',
            'author', 'reading_time', 'is_featured', 'published_date'
        ]

    def get_featured_image_url(self, obj):
        if obj.featured_image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.featured_image.url)
            return obj.featured_image.url
        return None


class ContactSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubmission
        fields = [
            'id', 'name', 'email', 'phone', 'service_type', 'message', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']

    def create(self, validated_data):
        return ContactSubmission.objects.create(**validated_data)


class SiteSettingsSerializer(serializers.ModelSerializer):
    logo_url = serializers.SerializerMethodField()
    favicon_url = serializers.SerializerMethodField()

    class Meta:
        model = SiteSettings
        fields = [
            'id', 'site_title_ar', 'site_title_en', 'site_description_ar', 'site_description_en',
            'contact_email', 'contact_phone', 'social_facebook', 'social_twitter',
            'social_instagram', 'social_linkedin', 'logo', 'logo_url', 'favicon', 'favicon_url',
            'updated_at'
        ]

    def get_logo_url(self, obj):
        if obj.logo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.logo.url)
            return obj.logo.url
        return None

    def get_favicon_url(self, obj):
        if obj.favicon:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.favicon.url)
            return obj.favicon.url
        return None
