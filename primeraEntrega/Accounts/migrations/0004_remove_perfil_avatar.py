# Generated by Django 4.1.3 on 2022-12-11 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_alter_perfil_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='avatar',
        ),
    ]
