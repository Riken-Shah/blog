# Generated by Django 3.1.1 on 2020-09-30 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dscblog', '0003_auto_20200929_1954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Title')),
                ('img_url', models.CharField(default=None, max_length=150, null=True)),
                ('content', models.CharField(default='', max_length=1500, verbose_name='Content')),
                ('created_on', models.DateTimeField()),
                ('modified_on', models.DateTimeField()),
                ('published_on', models.DateTimeField(default=None, null=True)),
                ('is_published', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
