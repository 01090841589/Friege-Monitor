# Generated by Django 3.0.3 on 2020-06-04 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApi', '0004_auto_20200604_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='contents',
            name='floor',
            field=models.IntegerField(default=1),
        ),
    ]
