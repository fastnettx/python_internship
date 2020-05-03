from django.urls import path
from . import views as my_views
from django.contrib.auth import views

urlpatterns = [
    path('', my_views.base, name='base'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('list_of_counries/', my_views.list_of_counries, name='list_of_counries'),
    path('list_of_counries/<int:country_id>/', my_views.show_the_city, name='detail_counries'),
    path('list_of_counries/<int:country_id>/<int:city_id>/', my_views.details_city, name='detail_city'),
    path('Sign_up/', my_views.sign_up, name='sign_up'),
]
