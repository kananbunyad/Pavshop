from django.db import models
from product.models import ProductVersion
from django.contrib.auth import get_user_model
User = get_user_model()
    

class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - Cart'

    @property
    def get_total(self):
        items=self.cart.all()
        return sum([item.get_total for item in items])


class CartItem(models.Model):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE,related_name='cart')
    product_version = models.ForeignKey(ProductVersion, on_delete=models.CASCADE,related_name='cart_product_version')
    quantity = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product_version.title} - {self.quantity}'
    
    @property
    def get_total(self):
        total=int(self.quantity) * self.product_version.price
        return total
    
 
class BillingAddress(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    phone_number = models.CharField(max_length=20)
    cart_id = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.first_name
     
        
       
        
       

