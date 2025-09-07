from django.contrib import admin
from .models import Member

class FormatMembers(admin.ModelAdmin):
    list_display = ("lastname", "firstname", "phone", "date_of_joining")
    list_per_page = 10
# Register your models here.
admin.site.register(Member, FormatMembers)				