from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    issue_date = models.DateField()
    publish = models.ForeignKey('Publish',on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=10)


class Publish(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)


class Book_Author(models.Model):
    book = models.ForeignKey('Book',on_delete=models.CASCADE)
    author = models.ForeignKey('Author',on_delete=models.CASCADE)