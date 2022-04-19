from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from applications.account.models import CustomUser
from main import settings

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
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='images', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')


class Rating(models.Model):
        product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='rating')
        owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rating')
        rating = models.SmallIntegerField(validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ])

class Review(models.Model):
    owner = models.ForeignKey(CustomUser, related_name='reviews', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner} --> {self.review}'


class Favorite(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True, on_delete=models.CASCADE,related_name='favorites')
    product = models.ForeignKey(Product,null=True,blank=True, on_delete=models.CASCADE, related_name='favorites')
    favorite = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.owner} --> {self.product}'




class Like(models.Model):
    owner = models.ForeignKey(CustomUser,blank=True,on_delete=models.CASCADE, related_name='like')
    product = models.ForeignKey(Product,blank=True, on_delete=models.CASCADE, related_name='like')

    class Meta:
        unique_together = ['owner', 'product']

    def __str__(self):
        return str(self.id)