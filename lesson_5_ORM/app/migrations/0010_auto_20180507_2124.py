# Generated by Django 2.0.5 on 2018-05-07 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_author_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.IntegerField()),
                ('author', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='publish',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.Publish'),
            preserve_default=False,
        ),
    ]
