# Generated by Django 4.1.3 on 2022-12-07 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTarea', '0004_comentario_delete_aula_delete_edificio'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='imagen',
            field=models.URLField(default=0),
            preserve_default=False,
        ),
    ]