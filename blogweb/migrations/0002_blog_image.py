# Generated by Django 4.2.7 on 2024-01-05 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
