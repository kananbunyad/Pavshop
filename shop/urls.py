"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,re_path,include
from account.views import activate
from shop import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from jet_django.urls import jet_urls
from django.conf.urls.i18n import i18n_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,


)

schema_view = get_schema_view(
   openapi.Info(
      title="Pavshop",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$',
        activate, name='activate'),
    path('social-auth/', include('social_django.urls', namespace="social")),
    re_path(r'^rosetta/', include('rosetta.urls')),
    path('api/', include('product.api.urls')),
    path('api/', include('account.api.urls',)),
    path('api/',include("checkout.api.urls")),
    path('jet_api/', include('jet_django.urls')),
    path('api/',include(("core.api.urls"), namespace='subscription')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



urlpatterns += i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('i18n/', include('django_translation_flags.urls')),
    path('', include('core.urls')),
    path('account/', include('account.urls')),
    path('product/', include('product.urls')),
    path('blog/', include('blog.urls')),
    path('cart/', include('checkout.urls')),
    path('', include('checkout.urls')),
)