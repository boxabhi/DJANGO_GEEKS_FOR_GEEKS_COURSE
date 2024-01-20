# Generated by Django 5.0 on 2024-01-20 16:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_abc'),
    ]

    operations = [
        migrations.AddField(
            model_name='abc',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='abc',
            name='this_field_is_from_basemodel',
            field=models.CharField(default='BASEMODEL', max_length=100),
        ),
        migrations.AddField(
            model_name='abc',
            name='update_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='college',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='college',
            name='this_field_is_from_basemodel',
            field=models.CharField(default='BASEMODEL', max_length=100),
        ),
        migrations.AddField(
            model_name='college',
            name='update_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='department',
            name='this_field_is_from_basemodel',
            field=models.CharField(default='BASEMODEL', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='this_field_is_from_basemodel',
            field=models.CharField(default='BASEMODEL', max_length=100),
        ),
        migrations.AddField(
            model_name='skills',
            name='this_field_is_from_basemodel',
            field=models.CharField(default='BASEMODEL', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='this_field_is_from_basemodel',
            field=models.CharField(default='BASEMODEL', max_length=100),
        ),
    ]