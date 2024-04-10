from django.urls import path
from .views import CartView,billingaddress,payment

app_name = 'checkout'
urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('order/', billingaddress, name='order'),
    path('payment/', payment, name='payment'),
]