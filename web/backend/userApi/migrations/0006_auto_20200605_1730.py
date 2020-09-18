# Generated by Django 3.0.3 on 2020-06-05 08:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userApi', '0005_contents_floor'),
    ]

    operations = [
        migrations.CreateModel(
            name='ingredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('section', models.CharField(blank=True, max_length=20)),
                ('floor', models.IntegerField(default=0)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('expire_date', models.CharField(max_length=10)),
                ('classification', models.CharField(max_length=30)),
                ('content', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='user',
        ),
        migrations.DeleteModel(
            name='Contents',
        ),
        migrations.DeleteModel(
            name='ingredient',
        ),
    ]
