from rest_framework import serializers
from rest_framework.utils import representation

from applications.product.models import Product, Image, Rating, Category, Likes


class ProductImageSerializers(serializers.ModelSerializer):    # сериализатор для обработки картинок
    class Meta:
        model = Image
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')         #owner - переопределяем это поле при входе, автоматически подгружай емейл, только для чтения. Не заполняем
    images = ProductImageSerializers(many=True, read_only=True)
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('id', 'owner','name','description','category','price','images','rating','like')      # Отображение полей в JSON формате на вывод всех продуктов, указываем какие поля

    def create(self, validated_data):       # переопределили, сохраняет вконце все что мы сделали
        request = self.context.get('request')       # context - сохран данные что передавали, вытаскиваем request
        images_data = request.FILES         # вытаскиваем все файлы из реквеста
        product = Product.objects.create(**validated_data)      ## Сохраним данные по запросу, без КАртинки.
        for image in images_data.getlist('images'):
            Image.objects.create(product=product, image=image)      # ОТ количества файлов прикрепленных, создадим лист полей, с указанием файлов, Можем соххранять несколько картин
        return product

    def to_representation(self, instance):          # Переопределили представление - Вывод средне арифметический Рейтинг
        representation = super().to_representation(instance)

        # print(representation)
        # representation['owner'] = 'ff'     # Для примера, переопределили вывод owner
        # print(instance)       # Вывод имен продуктов

        rating_result = 0
        for i in instance.rating.all():
            print(i)        # Это объект рейтинга
            rating_result += int(i.rating)
        # print(rating_result)        # Добавит все рейтинги по каждому товару = Сумму.

        if instance.rating.all().count()  == 0:
           representation['rating'] = rating_result
        else:
           representation['rating'] = rating_result/instance.rating.all().count()     # Вывод Средн Арифмет Рейтинг, присвоить в рейтинг






        return representation


class RatingSerializers(serializers.ModelSerializer):
    # owner = serializers.EmailField(required=False)
    class Meta:
        model = Rating
        # fields = '__all__'
        fields = ('rating',)

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = (
            'id',
            'body',
            'total_likes'
        )