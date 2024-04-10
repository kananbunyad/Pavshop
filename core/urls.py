from django.urls import path
from core.views import home, contact, about_us,export_view

app_name = 'core'

urlpatterns = [
    path('', home ,name='home'),
    path('contact/', contact, name='contact'),
    path('about-us/', about_us, name='about_us'),
    path('export/', export_view, name='export'),
]