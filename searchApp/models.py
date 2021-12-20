from django.db import models

class frontEndModel(models.Model):
    html_url=models.CharField(max_length=150)
    name=models.CharField(max_length=100,null=True)
    username=models.CharField(max_length=100)
    bio=models.CharField(max_length=250,null=True)
    mail=models.CharField(max_length=100,null=True)
    avatar_url=models.CharField(max_length=200,null=True)

class fullStackModel(models.Model):
    html_url=models.CharField(max_length=150)
    name=models.CharField(max_length=100,null=True)
    username=models.CharField(max_length=100)
    bio=models.CharField(max_length=250,null=True)
    mail=models.CharField(max_length=100,null=True)
    avatar_url=models.CharField(max_length=200,null=True)

class mobileDevModel(models.Model):
    html_url=models.CharField(max_length=150)
    name=models.CharField(max_length=100,null=True)
    username=models.CharField(max_length=100)
    bio=models.CharField(max_length=250,null=True)
    mail=models.CharField(max_length=100,null=True)
    avatar_url=models.CharField(max_length=200,null=True)

