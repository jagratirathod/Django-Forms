from django.db import models

class Register(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(blank=False,unique=True)
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile = models.BigIntegerField()
    married = models.CharField(max_length=30,null=True)
    unmarried = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    game  = models.CharField(max_length=30)
    file  = models.FileField(max_length=30,upload_to='upload/')
    image  = models.ImageField(upload_to='img/')
    date = models.DateTimeField()





