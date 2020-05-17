from django.contrib.auth.models import User, Group
from rest_framework import viewsets, views, response, permissions

from .serializers import UserSerializer, CountrySerializer
from locations.models import Country


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
