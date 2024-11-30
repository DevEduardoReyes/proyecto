# Generated by Django 5.1.3 on 2024-11-30 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0003_alter_plato_name_alter_plato_nombre_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='plato',
            name='imagen_plato',
            field=models.ImageField(null=True, upload_to='platos'),
        ),
        migrations.AddField(
            model_name='restaurante',
            name='logo',
            field=models.ImageField(null=True, upload_to='logos'),
        ),
    ]
