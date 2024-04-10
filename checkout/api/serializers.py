from rest_framework import serializers
from checkout.models import ShoppingCart, CartItem
from product.api.serializers import ProductDetaileSerializer


class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model=ShoppingCart
        fields=(
            'id',
            'user',
        )


class CartItemReadSerializer(serializers.ModelSerializer):
    product_version=ProductDetaileSerializer()
    cart=ShoppingCartSerializer()
    class Meta:
        model=CartItem
        fields=(
            'id',
            'product_version',
            'quantity',
            'cart',
        )

class CartItemCreateSerializer(serializers.ModelSerializer):
    
   

    class Meta:

        model=CartItem
        fields=(
            'id',
            'product_version',
            'quantity',
            'cart',
        )
    def create(self, validated_data):
        print(validated_data["cart"])

        try:
           cart=CartItem.objects.get(cart=validated_data["cart"],product_version=validated_data["product_version"])
           cart.quantity+=validated_data.get("quantity",1)
           cart.save()
           return cart
        except:

          return super().create(validated_data)

class CartItemDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartItem
        fields=(
           
            "quantity",
           
        )

    def update(self, instance, validated_data):
        quantity_change = validated_data.get('quantity', 0)
        instance.quantity += quantity_change


        if instance.quantity <= 0:
            instance.delete()
            return None
        else:
            instance.save()
            return instance



# class CartItemCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CartItem
#         fields = (
#             'id',
#             'cart',
#             'product_version',
#             'quantity',
#         )

#     def create(self, validated_data):
#         try:
#             cart_item = CartItem.objects.get(
#                 cart=validated_data["cart"],
#                 product_version=validated_data["product_version"]
#             )
#             # Increase quantity
#             cart_item.quantity += validated_data.get("quantity", 1)
#             cart_item.save()
#             return cart_item
#         except CartItem.DoesNotExist:
#             # If the cart item does not exist, create a new one
#             return super().create(validated_data)

    
