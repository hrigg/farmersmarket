# Generated by Django 4.1.2 on 2022-10-10 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_vendor_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='markets',
        ),
        migrations.AddField(
            model_name='market',
            name='vendor',
            field=models.ManyToManyField(to='main_app.vendor'),
        ),
    ]
