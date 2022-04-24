from functools import cached_property

from rest_framework import serializers
from rest_framework.utils import representation
from rest_framework.utils.field_mapping import get_nested_relation_kwargs

from applications.product.models import *



class ProductImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    images = ProductImageSerializers(many=True, read_only=True)

    class Meta:
        model = Product
        # fields = '__all__'
        # 'rating', 'likes'
        fields = ('id', 'owner','name','description','category','price','images','likes')

    def create(self, validated_data):
        request = self.context.get('request')

        images_data = request.FILES
        # pl=request.user_id
        product = Product.objects.create(**validated_data, owner=request.user)
        print(request.data)

        for image in images_data.getlist('images'):
            Image.objects.create(product=product, image=image)
        return product


#
    def to_representation(self, instance):
        representation = super().to_representation(instance)
#
#
#like_representation
        total_likes = 0
        for i in instance.likes.all():
            total_likes += 1

        representation['likes'] = total_likes

        return representation


class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('rating',)

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("review",)

class LikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = "__all__"

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class FavoriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = "__all__"
