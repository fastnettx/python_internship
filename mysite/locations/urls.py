from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('static_url/', views.static, name='static_url'),
    path('<slug:dynamic_url>/', views.dynamic, name='dynamic_url')
]
