# Generated by Django 5.0 on 2024-01-20 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_remove_student_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
