from django.urls import path
from . import views 

urlpatterns = [
    path('queryJoins/', views.queryJoins, name='queryJoins'),
    path('add/', views.addAuthorsAndBooks, name='addAuthorsAndBooks'),
]