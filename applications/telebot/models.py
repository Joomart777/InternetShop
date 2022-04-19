from django.db import models

class TeleSettings(models.Model):
    tg_token = models.CharField(max_length=200, verbose_name='Token')
    tg_chat_id = models.CharField(max_length=200, verbose_name='Chat_id')
    tg_message = models.TextField(verbose_name='Text message')

    def __str__(self):
        return self.tg_chat_id

    class Meta:
        verbose_name = 'Settingsnow'
        verbose_name_plural = 'Settings'
