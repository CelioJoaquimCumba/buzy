# Generated by Django 4.0 on 2022-01-26 19:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buzy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=160)),
                ('investement', models.DecimalField(decimal_places=3, max_digits=12)),
                ('gain', models.DecimalField(decimal_places=3, max_digits=12)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('participants', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=160)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('revenue', models.DecimalField(decimal_places=3, max_digits=12)),
                ('income', models.DecimalField(decimal_places=3, max_digits=12)),
                ('activity', models.ManyToManyField(to='buzy.Activity')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hosts', to='buzy.user')),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
