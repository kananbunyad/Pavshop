from rest_framework import serializers
from product.models import ProductCategory, Product, ProductTag, ProductVersion, ProductVersionImage, ProductVersionReview,Color,Brand, Wishlist
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model

USER = get_user_model()

class CustomObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(CustomObtainPairSerializer,cls).get_token(user)
        token['username'] = user.username

        return token

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = (
            'id',
            'title',
        )

class ProductBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'id',
            'title',
        )



class ProductTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductTag
        fields = (
            'id',
            'title',
        )

class ProductColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = (
            'id',
            'title',
            'hex_code'
        )



class ProductListReadSerializer(serializers.ModelSerializer):
    category=ProductCategorySerializer()
    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'cover_image',
            'description',
            'category',
            "brand",
            'slug'
        )


class ProductVersionImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVersionImage
        fields = ("image",)


class ProductDetaileSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    product=ProductListReadSerializer()
    tags=ProductTagSerializer(many=True)
    color=ProductColorSerializer(many=True)
    class Meta:
        model = ProductVersion
        fields = (
            'id',
            'title',
            'product',
            'description',
            'cover_image',
            'images',
            'quantity',
            'price',
            'tags',
            'color',
            "slug"
        )

    def get_images(self,obj):
        serializer=ProductVersionImageSerializer(obj.images.all(),many=True)

        return serializer.data
         
    
class ProductReviewReadSerializer(serializers.ModelSerializer):
    product_version=serializers.CharField(source='product_version.title')
    class Meta:
        model = ProductVersionReview
        fields = (
            'id',
            'product_version',
            'user',
            'comment',

        )


class ProductReviewCreateSerializer(serializers.ModelSerializer):
    user=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = ProductVersionReview
        fields = (
            'product_version',
            'user',
            'comment',
            
        )


    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return ProductVersionReview.objects.create(**validated_data)


class WishlistCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = (
            'id',
            'product_version',
            
        )
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user']=user
       
        wishlist=Wishlist.objects.filter(user=self.context['request'].user.id,product_version=validated_data["product_version"].id)
        if wishlist:
             error = {'message': 'Already liked'}
             raise serializers.ValidationError(error)
        else:
             return Wishlist.objects.create(**validated_data)


class WishlistReadSerializer(serializers.ModelSerializer):
    product_version=ProductDetaileSerializer()
    class Meta:
        model = Wishlist
        fields = (
            'id',
            'product_version',
            'user',
         )
    

class WishlistDeleteSerializer(serializers.ModelSerializer):
    product_version=ProductDetaileSerializer()
    class Meta:
        model = Wishlist
        fields = (
            'id',
            'product_version',
         )