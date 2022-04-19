from django.contrib import admin

# Register your models here.
from applications.telebot.models import TeleSettings

admin.site.register(TeleSettings)