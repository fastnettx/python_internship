from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Users', views.UserViewSet)
router.register(r'Countries', views.CountryViewSet, basename='Countries')

urlpatterns = [
    path('', include(router.urls)),
]
