from django.contrib import admin
from .models import Inventory

# Register your models here.
class FormatInventory(admin.ModelAdmin):
    list_display = ("name", "price", "category", "stock_quantity")
    list_per_page = 9
admin.site.register(Inventory, FormatInventory)
