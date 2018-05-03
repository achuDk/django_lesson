from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    issue_date = models.DateField()
    author = models.CharField(max_length=32,null=False)

# b1 = Book('python',123,'2018-05-03')


class Author(models.Model):
    author = models.CharField(max_length=30)