from django.urls import path
from core.api.views import NewsletterListCreateAPIView


app_name = 'api'
urlpatterns = [
    path('subscription/', NewsletterListCreateAPIView.as_view(), name='subscribtion'),

]
