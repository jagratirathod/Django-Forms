# Generated by Django 4.0.3 on 2022-03-03 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='gender',
            field=models.CharField(max_length=30),
        ),
    ]
