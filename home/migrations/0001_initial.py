# Generated by Django 5.0 on 2024-01-04 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(default='Male', max_length=100)),
                ('phone_number', models.CharField(max_length=10)),
                ('student_bio', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField()),
                ('student_registration', models.DateTimeField()),
                ('percentage', models.FloatField()),
            ],
        ),
    ]
