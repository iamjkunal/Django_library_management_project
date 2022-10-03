from django.db import models

# Create your models here.
class Books(models.Model):
    book_title=models.CharField(max_length=50)
    book_author=models.CharField(max_length=50)
    book_edition=models.CharField(max_length=50)
    book_place=models.CharField(max_length=50)
    book_publisher=models.CharField(max_length=50)
    book_year=models.PositiveIntegerField()



