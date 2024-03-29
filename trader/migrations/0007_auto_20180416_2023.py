# Generated by Django 2.0.2 on 2018-04-16 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trader', '0006_auto_20180410_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='status',
            field=models.CharField(choices=[('R', 'request'), ('A', 'approved')], default='R', max_length=100),
        ),
        migrations.AddField(
            model_name='trading',
            name='status',
            field=models.CharField(choices=[('O', 'open'), ('P', 'pending'), ('X', 'exchanging'), ('C', 'completed')], default='O', max_length=100),
        ),
        migrations.AlterField(
            model_name='trading',
            name='receiver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiving', to='trader.User'),
        ),
    ]
