# Generated by Django 4.1.2 on 2022-10-10 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_remove_vendor_markets_market_vendor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='market',
            old_name='vendor',
            new_name='vendors',
        ),
    ]
