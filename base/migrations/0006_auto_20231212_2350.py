# Generated by Django 3.2.8 on 2023-12-12 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20231212_2335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='imageTitle',
        ),
        migrations.AddField(
            model_name='blog',
            name='imageThumbnail',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
