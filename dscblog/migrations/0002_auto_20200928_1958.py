# Generated by Django 3.1.1 on 2020-09-28 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dscblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default=None, max_length=255, null=True, verbose_name='Email'),
        ),
    ]
