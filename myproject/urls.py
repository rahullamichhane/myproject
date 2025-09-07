from django.urls import include, path
from rest_framework import routers
from drf import views
from django.contrib import admin


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'books',views.BookViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('registration/', include('registration.urls')),
    path('api-auth/',include('rest_framework.urls', namespace='rest_framework'))
]
