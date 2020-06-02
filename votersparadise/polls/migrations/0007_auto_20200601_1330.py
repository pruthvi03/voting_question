# Generated by Django 3.0.5 on 2020-06-01 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0006_auto_20200601_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfollowing',
            name='profile_pic',
            field=models.ImageField(blank=True, default='', upload_to='polls/profile_pic'),
        ),
        migrations.AlterUniqueTogether(
            name='userfollowing',
            unique_together={('following', 'following')},
        ),
        migrations.RemoveField(
            model_name='userfollowing',
            name='followers',
        ),
        migrations.CreateModel(
            name='UserFollowers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('followers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('followers', 'followers')},
            },
        ),
    ]
