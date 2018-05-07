# Generated by Django 2.0.5 on 2018-05-07 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20180507_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_author',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Author'),
        ),
        migrations.AlterField(
            model_name='book_author',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Book'),
        ),
    ]
