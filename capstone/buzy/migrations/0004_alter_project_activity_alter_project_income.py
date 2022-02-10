# Generated by Django 4.0 on 2022-01-27 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buzy', '0003_user_following'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='activity',
            field=models.ManyToManyField(blank=True, to='buzy.Activity'),
        ),
        migrations.AlterField(
            model_name='project',
            name='income',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=12),
        ),
    ]