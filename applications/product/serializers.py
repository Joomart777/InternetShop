from rest_framework import serializers
from rest_framework.utils import representation


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

        fields = ('id', 'owner','name','description','category','price','images','rating','likes')
    def create(self, validated_data):
        request = self.context.get('request')
        images_data = request.FILES
        product = Product.objects.create(**validated_data)

        for image in images_data.getlist('images'):
            Image.objects.create(product=product, image=image)
        return product

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        rating_result = 0
        for i in instance.rating.all():
            print(i)
            rating_result += int(i.rating)
        # print(rating_result)
        if instance.rating.all().count()  == 0:
           representation['rating'] = rating_result
        else:
           representation['rating'] = rating_result/instance.rating.all().count()


##like_representation
        total_likes = 0
        for i in instance.likes.all():
            total_likes += 1
            print(i)
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
    # like = LikeTagSerializer(read_only=True, many=True).data
    class Meta:
        model = Likes
        fields = "__all__"

