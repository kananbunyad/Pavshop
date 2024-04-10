from django.db import models
from product.models import ProductVersion


# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.full_name
    


class Newsletter(models.Model):
    email = models.EmailField(max_length=100)
    subscription_status = models.BooleanField(default=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.email
    

class ReklamBanner(models.Model):
    product_version_id = models.ForeignKey(ProductVersion, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    title_color = models.CharField(max_length=20)
    title_font_size = models.IntegerField()
    link = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class SubBanner(models.Model):
    page = models.CharField(max_length=250)
    title = models.CharField(max_length=100)
    title_color = models.CharField(max_length=20)
    title_font_size = models.IntegerField()
    description = models.CharField(max_length=100)
    description_color = models.CharField(max_length=20)
    description_font_size = models.IntegerField()
    breadcrumbs = models.CharField(max_length=255)
    image = models.ImageField(max_length=255)
    is_active = models.BooleanField(default=True)


    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title