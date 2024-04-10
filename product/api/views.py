from .serializers import *
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly,AllowAny
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,ListAPIView
from product.models import ProductCategory, Product,ProductVersion,ProductVersionReview,Color,Brand,ProductTag
from rest_framework.response import Response


class LimitPagination(PageNumberPagination):
    page_size = 2
    def get_paginated_response(self, data):
        return Response({
            'total': self.page.paginator.count,
            'current_page': self.page.number,
            'last_page': self.page.paginator.num_pages,
            'results': data
        })

class ProductListReadAPIView(ListAPIView):
    
    serializer_class = ProductDetaileSerializer
    queryset = ProductVersion.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['product__category__title', 'product__brand__title','tags__title','color__title']
    search_fields = ['title']
    pagination_class=LimitPagination
    # def get(self, request, *args, **kwargs):
        
    #     serializer = ProductDetaileSerializer(self.get_queryset(), many=True)
    #     page = self.paginate_queryset(serializer.data)
    #     return self.get_paginated_response(page)


class ProductColorReadAPIView(ListAPIView):
    
    serializer_class = ProductColorSerializer
    queryset = Color.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ProductBrandReadAPIView(ListAPIView):
    
    serializer_class = ProductBrandSerializer
    queryset = Brand.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ProductTagReadAPIView(ListAPIView):
    
    serializer_class = ProductTagSerializer
    queryset = ProductTag.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ProductDetailReadAPIView(ListAPIView):
   
    serializer_class = ProductDetaileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        
        queryset = ProductVersion.objects.all()
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category__name=category)

        return queryset    

    
class ProductCategoryReadAPIView(ListAPIView):
 
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ProductVersionReviewCreateAPIView(ListCreateAPIView):
    
    serializer_class = ProductReviewReadSerializer
    queryset = ProductVersionReview.objects.all()
    permission_classes = ([])

    def post(self, request, *args, **kwargs):
        
        return super().post(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            self.serializer_class = ProductReviewCreateSerializer

        return super().get_serializer_class()
    

class WishlistCreateAPIView(ListCreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistReadSerializer 
    permission_classes= (IsAuthenticated,)

    def get_serializer_class(self):

        if self.request.method == 'POST':
            return WishlistCreateSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        user = self.request.user 
        serializer.save(user=user)
    
    
class WishlistItemDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = WishlistDeleteSerializer
    queryset = Wishlist.objects.all()
    permission_classes = (IsAuthenticated,)


    def destroy(self, request, *args, **kwargs):

        return super().destroy(request, *args, **kwargs)