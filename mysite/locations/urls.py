from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('staticUrl/', views.static, name='staticUrl'),
    path('<slug:dynamicUrl>/', views.dynamic, name='dynamicUrl')
]
