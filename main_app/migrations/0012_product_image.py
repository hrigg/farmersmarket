# Generated by Django 4.1.2 on 2022-10-11 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(default='https://media.istockphoto.com/', max_length=300),
        ),
    ]
