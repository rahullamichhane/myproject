from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addinventory, name='addinventory'),
    path('view/', views.viewinventory, name='viewinventory'),
]
    

    