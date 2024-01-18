from django.db import models

# Create your models here.
class UserProfile(models.Model):
    # image=models.FileField(upload_to='images')
    slug=models.CharField(max_length=120,null=True)
    date=models.DateField(null=True)
    content=models.CharField(max_length=1000,null=True)
    title=models.CharField(max_length=120,null=True)
    extract=models.CharField(max_length=200,null=True)
    author=models.CharField(max_length=120,null=True)
    postedBy=models.CharField(max_length=120,null=True)
    image=models.ImageField(upload_to='images')
