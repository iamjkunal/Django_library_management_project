from django.contrib import admin
from library.models import Books
# Register your models here.
class bookdetails(admin.ModelAdmin):
    list_display=( 'book_title','book_author','book_edition','book_place','book_publisher','book_year')

admin.site.register(Books,bookdetails)
