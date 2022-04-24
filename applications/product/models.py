from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# from applications.likes.models import Like

from applications.account.models import CustomUser


User = get_user_model()

# Create your models here.
class Category(models.Model):
    slug = models.SlugField(max_length=30, primary_key=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.slug

class Product(models.Model):
    owner = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='images', null=True, blank=True)
    def __str__(self):
        return f'{self.name}'



class Image(models.Model):

    image = models.ImageField(upload_to='images', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')


class Rating(models.Model):
        product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='rating')
        owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rating')
        rating = models.SmallIntegerField(validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ])



class Review(models.Model):
    owner = models.ForeignKey(CustomUser, related_name='comments', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner} --> {self.product}'



class Likes(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='likes')
    # owner = models.OneToOneField(User, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like')

    def __str__(self):
        return f'{self.owner}--likes-> {self.product}'


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order')
    customer = models.CharField(verbose_name='Your name', max_length=30)
    tel = models.CharField(verbose_name='Your tel',max_length=30, blank=False)
    quantity = models.PositiveIntegerField(verbose_name='Quantity', blank=False)

    def __str__(self):
        return f'{self.customer}--ordered-> {self.product}'


class Favorite(models.Model):
    owner = models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE,related_name='favorites')
    product = models.ForeignKey(Product,null=True,blank=True, on_delete=models.CASCADE, related_name='favorites')
    favorite = models.BooleanField(default=True)

    def str(self):
        return f'{self.owner} --> {self.product}'