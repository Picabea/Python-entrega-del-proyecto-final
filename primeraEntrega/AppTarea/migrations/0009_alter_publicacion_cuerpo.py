# Generated by Django 4.1.3 on 2022-12-12 14:15

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTarea', '0008_alter_publicacion_cuerpo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='cuerpo',
            field=tinymce.models.HTMLField(),
        ),
    ]
