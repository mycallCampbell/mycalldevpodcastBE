# Generated by Django 3.2.8 on 2023-12-12 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20231212_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='imageHeight',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='imageWidth',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
