# Generated by Django 2.0.2 on 2018-04-23 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trader', '0008_auto_20180416_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('detail', models.CharField(blank=True, default='', max_length=200)),
                ('deleted', models.BooleanField(default=False)),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trader.Basket')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trader.User')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
