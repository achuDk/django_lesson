# Generated by Django 2.0.4 on 2018-05-07 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_book_authors_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publish',
        ),
        migrations.RemoveField(
            model_name='book_authors',
            name='name',
        ),
    ]
