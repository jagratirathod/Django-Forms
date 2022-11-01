# Generated by Django 4.0.3 on 2022-03-03 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoform', '0004_alter_register_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='file',
            field=models.FileField(max_length=30, upload_to='upload/'),
        ),
        migrations.AlterField(
            model_name='register',
            name='image',
            field=models.ImageField(upload_to='upload/'),
        ),
    ]
