# Generated by Django 4.1.3 on 2022-12-06 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTarea', '0002_aula_edificio_delete_estudiante_delete_profesor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('subtitulo', models.CharField(max_length=50)),
                ('cuerpo', models.CharField(max_length=200)),
            ],
        ),
    ]
