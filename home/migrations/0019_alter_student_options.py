# Generated by Django 5.0 on 2024-01-20 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_alter_student_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['-name']},
        ),
    ]
