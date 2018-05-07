from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    issue_date = models.DateField()

    """ 外键要建立在“一对多”中多所对应的一方，且外键关联另一张表的字段必须是主键"""


    publish = models.ForeignKey("Publish",on_delete=models.CASCADE)

    author = models.ForeignKey("Author",on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Publish(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.name