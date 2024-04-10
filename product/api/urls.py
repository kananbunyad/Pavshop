from django.urls import path
from product.api.views import (
    ProductListReadAPIView,
    ProductBrandReadAPIView,
    ProductDetailReadAPIView,
    ProductCategoryReadAPIView,
    ProductVersionReviewCreateAPIView,
    ProductColorReadAPIView,
    ProductTagReadAPIView,
    WishlistCreateAPIView,
    WishlistItemDeleteAPIView
    
)
# from story.api.router import router

app_name = 'api'
urlpatterns = [
    path('product/', ProductListReadAPIView.as_view(), name='products'),
    path('product/<int:pk>/', ProductDetailReadAPIView.as_view(), name='product'),
    path('category/', ProductCategoryReadAPIView.as_view(), name='category'),
    path('brand/', ProductBrandReadAPIView.as_view(), name='brand'),
    path('color/', ProductColorReadAPIView.as_view(), name='color'),
    path('tag/', ProductTagReadAPIView.as_view(), name='tag'),
    path('product/review/', ProductVersionReviewCreateAPIView.as_view(), name='reviews'),
    path('wishlists/', WishlistCreateAPIView.as_view(), name='wishlist-list'),
    path('wishlists/create/', WishlistCreateAPIView.as_view(), name='wishlist-create'),
    path("delete_wishlist/<int:pk>",WishlistItemDeleteAPIView.as_view(),name="wishlistdelete")
]

