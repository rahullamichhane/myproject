#serializer => Convert the code into JSON
from django.contrib.auth.models import User, Group
from rest_framework import routers, serializers, viewsets #Rest_framework APIs
from author.models import Book,Author
from django.db import models

# Dealing with nested objects
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email','is_staff']
        
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name',] 
        
class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['url','name']
        
class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['url','title']
        
        



    
        

   
    