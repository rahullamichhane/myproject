from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name="members"),
    path('addusers/', views.addusers, name="addusers"),
    path('deleteusers/', views.deleteusers, name="deleteusers"),
    path('members/details/<int:id>', views.details, name='details'),
    path('test/', views.test, name="test"),
]