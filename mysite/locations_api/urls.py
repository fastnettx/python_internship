from django.urls import path, include
from rest_framework import routers
from . import views
from .yasg import urlpatterns as url_yasg

router = routers.DefaultRouter()
router.register(r'city_filter', views.CityFilterViewSet, basename='city_filter')
router.register(r'city', views.CityViewSet, basename='list_of_city')

urlpatterns = [
    path('', include(router.urls)),
    path('country/', views.CountryAPIView.as_view(), name='list_of_country'),
    path('country/<int:pk>/', views.CountryDetailAPIView.as_view(), name='country_change'),
    path('country/delete<int:pk>/', views.CountryDeleteAPIView.as_view(), name='country_delete'),
    path('country/create/', views.CountryCreateAPIView.as_view(),  name='country_create'),
    path('filter/', views.CityFilterAPIView.as_view()),
    path('accounts/', include('rest_framework.urls')),
    path('user_create/', views.CreateUserAPIView.as_view()),
    path('google_login/', views.SignInGoogleAPIView.as_view()),
]
urlpatterns += url_yasg
