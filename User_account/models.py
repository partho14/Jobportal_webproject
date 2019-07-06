from django.db import models

class userinfo(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    date_of_birth = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    educational_info = models.CharField(max_length=250)

class user(models.Model):
    user_type_id = models.ForeignKey(userinfo,on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
