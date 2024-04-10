from django.db import models
from django.db.models.fields.files import ImageField
from django.contrib.auth import get_user_model



User = get_user_model()


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    cover_image = ImageField(upload_to='blog_cover_images')
    content = models.TextField()
    is_active = models.BooleanField(default=True)
    view_count = models.IntegerField()
    slug = models.SlugField(unique=True,max_length=50)
    tags = models.ManyToManyField('BlogTag',related_name='blogs')
    categories = models.ForeignKey('BlogCategory',on_delete=models.CASCADE,related_name='blogcategory')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    


class Comments(models.Model):
    blog_id = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name="comments")
    parent_id = models.ForeignKey('Comments',on_delete=models.CASCADE,null=True,blank=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    comment = models.TextField()

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.full_name
    
class BlogCategory(models.Model):

    title = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True,max_length=50)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    

class BlogTag(models.Model):

    title = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True,max_length=50)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title