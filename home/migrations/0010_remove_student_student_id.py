# Generated by Django 5.0 on 2024-01-20 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_student_student_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student_id',
        ),
    ]
