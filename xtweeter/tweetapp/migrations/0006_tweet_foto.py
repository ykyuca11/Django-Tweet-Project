# Generated by Django 5.0.6 on 2024-07-11 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweetapp', '0005_tweetlike'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='foto',
            field=models.ImageField(null=True, upload_to='uploads'),
        ),
    ]
