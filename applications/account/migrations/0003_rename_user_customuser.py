# Generated by Django 4.0.3 on 2022-04-14 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('authtoken', '0003_tokenproxy'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('account', '0002_rename_customuser_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='CustomUser',
        ),
    ]
