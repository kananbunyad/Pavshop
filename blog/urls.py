from django.urls import path
from blog.views import blog,blog_detail

app_name = 'blog'
urlpatterns = [
    path('blog/', blog, name='blog'),
    path('blog/<slug:slug>', blog_detail, name='blog-detail'),
]