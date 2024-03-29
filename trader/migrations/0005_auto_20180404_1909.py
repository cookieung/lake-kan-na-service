# Generated by Django 2.0.2 on 2018-04-04 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trader', '0004_auto_20180401_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='trading',
            name='description',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='trading',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.CharField(choices=[('V', 'visible'), ('I', 'invisible')], default='visible', max_length=100),
        ),
    ]
