# Generated by Django 5.0 on 2024-01-26 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_contact_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files'),
        ),
    ]