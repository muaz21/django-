from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.utils import timezone
from .models import (
    HeroSection, PricingPackage, Service, Portfolio, 
    BlogPost, ContactSubmission, SiteSettings
)
from .serializers import (
    HeroSectionSerializer, PricingPackageSerializer, ServiceSerializer,
    PortfolioSerializer, BlogPostSerializer, BlogPostListSerializer,
    ContactSubmissionSerializer, SiteSettingsSerializer
)


class HeroSectionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for hero sections - read only for public API
    """
    queryset = HeroSection.objects.filter(is_active=True)
    serializer_class = HeroSectionSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['get'])
    def active(self, request):
        """Get the currently active hero section"""
        hero = self.queryset.first()
        if hero:
            serializer = self.get_serializer(hero)
            return Response(serializer.data)
        return Response({'detail': 'No active hero section found'}, status=status.HTTP_404_NOT_FOUND)


class PricingPackageViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for pricing packages - read only for public API
    """
    queryset = PricingPackage.objects.filter(is_active=True)
    serializer_class = PricingPackageSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [OrderingFilter]
    ordering_fields = ['order', 'price']
    ordering = ['order', 'price']

    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get popular/featured pricing packages"""
        packages = self.queryset.filter(is_popular=True)
        serializer = self.get_serializer(packages, many=True)
        return Response(serializer.data)


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for services - read only for public API
    """
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'is_featured']
    search_fields = ['title_ar', 'title_en', 'description_ar', 'description_en']
    ordering_fields = ['order', 'created_at']
    ordering = ['category', 'order']

    @action(detail=False, methods=['get'])
    def by_category(self, request):
        """Get services grouped by category"""
        categories = Service.SERVICE_CATEGORIES
        result = {}
        
        for category_code, category_name in categories:
            services = self.queryset.filter(category=category_code)
            serializer = self.get_serializer(services, many=True)
            result[category_code] = {
                'name': category_name,
                'services': serializer.data
            }
        
        return Response(result)

    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get featured services"""
        services = self.queryset.filter(is_featured=True)
        serializer = self.get_serializer(services, many=True)
        return Response(serializer.data)


class PortfolioViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for portfolio projects - read only for public API
    """
    queryset = Portfolio.objects.filter(is_active=True)
    serializer_class = PortfolioSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'is_featured']
    search_fields = ['title_ar', 'title_en', 'description_ar', 'description_en']
    ordering_fields = ['completed_date', 'order']
    ordering = ['-completed_date', 'order']

    @action(detail=False, methods=['get'])
    def by_category(self, request):
        """Get portfolio projects grouped by category"""
        categories = Portfolio.PROJECT_CATEGORIES
        result = {}
        
        for category_code, category_name in categories:
            projects = self.queryset.filter(category=category_code)
            serializer = self.get_serializer(projects, many=True)
            result[category_code] = {
                'name': category_name,
                'projects': serializer.data
            }
        
        return Response(result)

    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get featured portfolio projects"""
        projects = self.queryset.filter(is_featured=True)
        serializer = self.get_serializer(projects, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def recent(self, request):
        """Get recent portfolio projects"""
        projects = self.queryset.order_by('-completed_date')[:6]
        serializer = self.get_serializer(projects, many=True)
        return Response(serializer.data)


class BlogPostViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for blog posts - read only for public API
    """
    queryset = BlogPost.objects.filter(status='published', published_date__lte=timezone.now())
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['is_featured', 'category_en']
    search_fields = ['title_ar', 'title_en', 'excerpt_ar', 'excerpt_en', 'content_ar', 'content_en']
    ordering_fields = ['published_date', 'reading_time']
    ordering = ['-published_date']
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return BlogPostListSerializer
        return BlogPostSerializer

    def get_object(self):
        """
        Override to support both slug and ID lookup
        """
        lookup_value = self.kwargs.get(self.lookup_field)
        
        # Try to find by slug first
        try:
            return self.queryset.get(slug=lookup_value)
        except BlogPost.DoesNotExist:
            # If not found by slug, try by ID
            try:
                return self.queryset.get(id=lookup_value)
            except (BlogPost.DoesNotExist, ValueError):
                # If ID is not a valid integer, raise 404
                from django.http import Http404
                raise Http404("Blog post not found")

    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get featured blog posts"""
        posts = self.queryset.filter(is_featured=True)[:3]
        serializer = BlogPostListSerializer(posts, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def recent(self, request):
        """Get recent blog posts"""
        posts = self.queryset.order_by('-published_date')[:6]
        serializer = BlogPostListSerializer(posts, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def categories(self, request):
        """Get all blog categories"""
        # Get unique categories from published posts
        categories_ar = self.queryset.values_list('category_ar', flat=True).distinct()
        categories_en = self.queryset.values_list('category_en', flat=True).distinct()
        
        # Combine and create category pairs
        categories = []
        for cat_ar, cat_en in zip(categories_ar, categories_en):
            if cat_ar and cat_en:
                categories.append({
                    'name_ar': cat_ar,
                    'name_en': cat_en,
                    'post_count': self.queryset.filter(category_ar=cat_ar).count()
                })
        
        return Response(categories)


class ContactSubmissionViewSet(viewsets.ModelViewSet):
    """
    ViewSet for contact submissions - create only for public API
    """
    queryset = ContactSubmission.objects.all()
    serializer_class = ContactSubmissionSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_permissions(self):
        """
        Only allow create operations for public API
        """
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
    
    def list(self, request, *args, **kwargs):
        """Disable list view for public API"""
        return Response({'detail': 'Not allowed'}, status=status.HTTP_403_FORBIDDEN)

    def create(self, request, *args, **kwargs):
        """Create a new contact submission"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        # Return success message without exposing the created object
        return Response(
            {'message': 'Your message has been sent successfully. We will contact you soon.'},
            status=status.HTTP_201_CREATED
        )


class SiteSettingsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for site settings - read only for public API
    """
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['get'])
    def current(self, request):
        """Get current site settings"""
        settings = self.queryset.first()
        if settings:
            serializer = self.get_serializer(settings)
            return Response(serializer.data)
        return Response({'detail': 'Site settings not configured'}, status=status.HTTP_404_NOT_FOUND)
