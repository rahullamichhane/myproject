from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q, Sum, Avg
from .models import Inventory

# Create your views here.

#Creation of products
def addinventory(request):
    Inventory.objects.create(name="Laptop",category="Electronics",price=1000,stock_quantity=25)
    Inventory.objects.create(name="TV",category="Electronics",price=499.99,stock_quantity=50)
    Inventory.objects.create(name="Headphones",category="Electronics",price=799.99,stock_quantity=48)
    Inventory.objects.create(name="T-Shirts",category="Clothing",price=29.49,stock_quantity=78)
    Inventory.objects.create(name="Tablets",category="Electronics",price=399.99,stock_quantity=96)
    return HttpResponse("All items are saved to the DB",request)

def viewinventory(request):
  items = Inventory.objects.order_by('name')
  electronic_products = Inventory.objects.filter(category="Electronics")
  total_price = electronic_products.aggregate(total_price=Sum('price'))
  avg_price = electronic_products.aggregate(avg_price=Avg('price'))
  

  template = loader.get_template('items.html')  
  context = {
    'items': items,
    'total_electronics_price': total_price,
    'avg_price': avg_price
  }
  return HttpResponse(template.render(context, request))
   
    