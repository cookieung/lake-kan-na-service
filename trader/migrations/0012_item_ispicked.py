# Generated by Django 2.0.2 on 2018-04-25 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trader', '0011_trader_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='isPicked',
            field=models.BooleanField(default=False),
        ),
    ]
