# Generated by Django 3.0.5 on 2020-05-24 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfollowing',
            name='profile_pic',
            field=models.ImageField(default='', upload_to='polls/profile_pic'),
        ),
    ]
