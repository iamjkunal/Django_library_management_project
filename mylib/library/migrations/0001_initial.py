# Generated by Django 4.1 on 2022-10-02 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=50)),
                ('book_author', models.CharField(max_length=50)),
                ('book_edition', models.CharField(max_length=50)),
                ('book_place', models.CharField(max_length=50)),
                ('book_publisher', models.CharField(max_length=50)),
                ('book_year', models.IntegerField(max_length=5)),
            ],
        ),
    ]
