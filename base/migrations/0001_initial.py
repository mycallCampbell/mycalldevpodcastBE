# Generated by Django 3.2.8 on 2023-11-21 00:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('goLive', models.CharField(blank=True, max_length=200, null=True)),
                ('imageTitle', models.CharField(blank=True, max_length=200, null=True)),
                ('imageRef1', models.CharField(blank=True, max_length=200, null=True)),
                ('imageRef2', models.CharField(blank=True, max_length=200, null=True)),
                ('imageRef3', models.CharField(blank=True, max_length=200, null=True)),
                ('minuteRead', models.IntegerField(blank=True, default=0, null=True)),
                ('blogTitle', models.CharField(blank=True, max_length=200, null=True)),
                ('subTitle1', models.CharField(blank=True, max_length=200, null=True)),
                ('subTitle2', models.CharField(blank=True, max_length=200, null=True)),
                ('subTitle3', models.CharField(blank=True, max_length=200, null=True)),
                ('subTitle4', models.CharField(blank=True, max_length=200, null=True)),
                ('caption1', models.CharField(blank=True, max_length=200, null=True)),
                ('caption2', models.CharField(blank=True, max_length=200, null=True)),
                ('captchaPhrase', models.TextField(blank=True, null=True)),
                ('callToAction1', models.TextField(blank=True, null=True)),
                ('callToAction2', models.TextField(blank=True, null=True)),
                ('callToAction3', models.TextField(blank=True, null=True)),
                ('description1', models.TextField(blank=True, null=True)),
                ('description2', models.TextField(blank=True, null=True)),
                ('description3', models.TextField(blank=True, null=True)),
                ('description4', models.TextField(blank=True, null=True)),
                ('description5', models.TextField(blank=True, null=True)),
                ('description6', models.TextField(blank=True, null=True)),
                ('description7', models.TextField(blank=True, null=True)),
                ('description8', models.TextField(blank=True, null=True)),
                ('description9', models.TextField(blank=True, null=True)),
                ('description10', models.TextField(blank=True, null=True)),
                ('description11', models.TextField(blank=True, null=True)),
                ('createAt', models.DateTimeField(auto_now_add=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]