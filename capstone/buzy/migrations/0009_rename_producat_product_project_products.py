# Generated by Django 4.0 on 2022-01-30 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buzy', '0008_activity_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Producat',
            new_name='Product',
        ),
        migrations.AddField(
            model_name='project',
            name='products',
            field=models.ManyToManyField(blank=True, to='buzy.Product'),
        ),
    ]
