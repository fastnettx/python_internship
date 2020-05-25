from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'city_filter', views.CityFilterSet, basename='city_filter')
router.register(r'city', views.CityViewSet, basename='city')

urlpatterns = [
    path('', include(router.urls)),
    path('country/', views.CountryViewSet.as_view()),
    path('country/<int:pk>/', views.CountryDetailViewSet.as_view()),
    path('country/delete<int:pk>/', views.CountryDelete.as_view()),
    path('country/create/', views.CountryCreateAPIView.as_view()),
    path('filter/', views.CityFilterTest.as_view()),
]
