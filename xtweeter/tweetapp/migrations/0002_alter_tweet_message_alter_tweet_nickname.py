# Generated by Django 5.0.6 on 2024-07-10 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweetapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='message',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='nickname',
            field=models.CharField(max_length=30),
        ),
    ]
