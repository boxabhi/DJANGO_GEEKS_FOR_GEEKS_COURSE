# Generated by Django 5.0 on 2024-01-20 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_merge_20240120_2211'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='college',
            options={},
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_id',
        ),
    ]
