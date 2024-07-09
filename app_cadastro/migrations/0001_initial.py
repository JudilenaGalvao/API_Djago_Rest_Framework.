# Generated by Django 5.0.6 on 2024-07-09 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('price', models.FloatField(default='0')),
                ('description', models.CharField(default='', max_length=100)),
                ('categories', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
