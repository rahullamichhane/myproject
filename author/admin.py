from django.contrib import admin
from django.contrib import admin
from .models import Author,Book

# Register your models here.
class FormatAuthor(admin.ModelAdmin):
    list_display = ("name", "country")
admin.site.register(Author, FormatAuthor)

# @admin.register(Book) => we can register in this way or in another way i.e line 8 or 13
class FormatBook(admin.ModelAdmin):
    list_display = ("title", "author")
admin.site.register(Book, FormatBook)

