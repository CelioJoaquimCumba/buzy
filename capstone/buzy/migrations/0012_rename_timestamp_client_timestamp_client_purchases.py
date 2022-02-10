# Generated by Django 4.0 on 2022-02-02 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buzy', '0011_project_clients'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='Timestamp',
            new_name='timestamp',
        ),
        migrations.AddField(
            model_name='client',
            name='purchases',
            field=models.ManyToManyField(blank=True, to='buzy.Product'),
        ),
    ]