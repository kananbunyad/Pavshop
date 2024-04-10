from django.urls import path
from product.views import products, product_detail,WishlistView

app_name = 'product'
urlpatterns = [
    path('product/', products, name='products'),
    path('product/<slug:slug>', product_detail, name='product-detail'),
      path('wishlist/', WishlistView.as_view(), name='wishlist'),
]