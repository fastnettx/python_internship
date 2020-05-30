from django.urls import path, include
from rest_framework import routers
from . import views
from .yasg import urlpatterns as url_yasg

router = routers.DefaultRouter()
router.register(r'city_filter', views.CityFilterViewSet, basename='city_filter')
router.register(r'city', views.CityViewSet, basename='city')

urlpatterns = [
    path('', include(router.urls)),
    path('country/', views.CountryAPIView.as_view()),
    path('country/<int:pk>/', views.CountryDetailAPIView.as_view()),
    path('country/delete<int:pk>/', views.CountryDeleteAPIView.as_view()),
    path('country/create/', views.CountryCreateAPIView.as_view()),
    path('filter/', views.CityFilterAPIView.as_view()),
    path('accounts/', include('rest_framework.urls')),
    path('user_create/', views.CreateUserAPIView.as_view()),
    path('google_login/', views.SignInGoogleAPIView.as_view()),
]
urlpatterns += url_yasg
