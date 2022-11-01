# Generated by Django 4.0.3 on 2022-03-03 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('mobile', models.BigIntegerField()),
                ('married', models.CharField(max_length=30, null=True)),
                ('unmarried', models.CharField(max_length=30)),
                ('gender', models.BooleanField(max_length=30)),
                ('game', models.CharField(max_length=30)),
                ('file', models.FileField(max_length=30, upload_to='')),
                ('image', models.ImageField(max_length=30, upload_to='')),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
