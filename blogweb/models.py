from django.db import models

class Blog(models.Model):
    slug=models.CharField(max_length=120)
    date=models.DateField()
    content=models.CharField(max_length=1000)
    title=models.CharField(max_length=120)
    extract=models.CharField(max_length=200)
    author=models.CharField(max_length=120)
    postedBy=models.CharField(max_length=120)


# Create your models here.

    def __str__(self):
        return f'{self.author} and {self.title}'