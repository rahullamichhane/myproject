from django.contrib import admin
from django.urls import  include, path
from django.conf import settings
from django.conf.urls.static import static
from drf import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from users import views as user_views
from rest_framework import serializers, viewsets , routers


admin.site.site_header = "Website Administration"
admin.site.site_title = "Site Administration"
admin.site.index_title = "Login Portel"



urlpatterns = [
    # path('members', include('members.urls')),
    path('admin/', admin.site.urls),
    path('inventory/', include('inventory.urls')),
    path('author/', include('author.urls')),
    path('registration/', include('registration.urls')),
    path('register/', user_views.register, name='register'),
    path('', user_views.home, name = 'home'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    
   
    path('api-auth/',include('rest_framework.urls', namespace='rest_framework')),
 
]




# Add the following lines to serve media and static files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
