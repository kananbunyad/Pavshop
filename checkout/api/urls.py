from django.urls import path
from .views import CartItemCreateAPIView,CartItemDeleteAPIView

urlpatterns = [
    path("create_order",CartItemCreateAPIView.as_view(),name="ordercreate"),
    path("delete_order/<int:pk>",CartItemDeleteAPIView.as_view(),name="orderdelete")

]