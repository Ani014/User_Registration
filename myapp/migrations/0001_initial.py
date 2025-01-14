# Generated by Django 5.0.1 on 2024-07-16 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=20)),
                ('email', models.EmailField(default='', max_length=254)),
                ('password1', models.CharField(default='', max_length=50)),
                ('password2', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
