from django.db import models
from django.db.models.fields.files import ImageField
from django.contrib.auth import get_user_model
from slugify import slugify
User = get_user_model()


class Brand(models.Model):
    title = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ProductTag(models.Model):
    title = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ProductCategory(models.Model):
    title = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,related_name='product_brand')
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True,blank=True, max_length=200)
    cover_image = ImageField(upload_to='product_version_image',null=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE,related_name='product_category')
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=200)
    hex_code = models.CharField(max_length=7)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProductVersion(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='product')
    color = models.ManyToManyField(Color, blank=True)
    title = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    # discount_percent = models.IntegerField(default=0)
    quantity = models.IntegerField()
    tags = models.ManyToManyField(ProductTag, blank=True,related_name='tag')
    description = models.TextField(blank=True)
    cover_image = ImageField(upload_to='product_version_image')
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(null=True,blank=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_reviews(self):
        raitings=sum([ raiting for raiting in self.product.version.all()])
        overall=raitings // len([ raiting for raiting in self.product.version.all()])

        return  overall
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        return super(ProductVersion,self).save()
    


class ProductVersionImage(models.Model):
    product_version = models.ForeignKey(ProductVersion, on_delete=models.CASCADE,related_name="images")
    image = ImageField(upload_to='product_version_images')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.product_version)
    



class ProductVersionReview(models.Model):
    product_version = models.ForeignKey(ProductVersion, on_delete=models.CASCADE,related_name='product_version')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='product_version_user')
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    comment = models.TextField()
    raiting=models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.full_name} - {self.product_version.title}'


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='wishlist_user')
    product_version = models.ForeignKey(ProductVersion, on_delete=models.CASCADE,related_name='wishlist_product')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.product_version.title} Wishlist'