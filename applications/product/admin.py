from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group

from applications.product.models import *

admin.site.register(Category)
# admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Rating)       # Чтобы видеть в Админке, зарегили эту модельку - рейтинг

admin.site.unregister(Group)        # Дерегистрируем Группы - автоматом появляется при создании Аккаунтов

# admin.site.register(Like)

class ImageInAdmin(admin.TabularInline):
    model = Image
    fields = ('image',)
    max_num = 3

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ImageInAdmin
    ]


