# Generated by Django 5.0 on 2024-01-06 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_student_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
