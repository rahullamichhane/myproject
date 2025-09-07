from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Inventory(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}"
        
    
