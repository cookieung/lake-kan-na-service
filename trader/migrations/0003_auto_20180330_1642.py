# Generated by Django 2.0.2 on 2018-03-30 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trader', '0002_auto_20180326_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(blank=True, default='', max_length=100)),
                ('password', models.CharField(blank=True, default='', max_length=100)),
                ('deleted', models.BooleanField(default=False)),
                ('trader_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trader.Trader')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.AlterField(
            model_name='basket',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trader.User'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trader.User'),
        ),
        migrations.AlterField(
            model_name='review',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trader.User'),
        ),
        migrations.AlterField(
            model_name='trading',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trading', to='trader.User'),
        ),
        migrations.AlterField(
            model_name='trading',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiving', to='trader.User'),
        ),
    ]
