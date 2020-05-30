from rest_framework import viewsets, permissions, generics, views
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
import requests
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.utils import json
from .serializers import (CountrySerializer, CitySerializer, CityFilterSerializer,
                          CountryDetailSerializer, FilterCitySerializer, UserSerializer, GoogleSerializer)
from django_filters.rest_framework import DjangoFilterBackend
from locations.models import Country, City


class CreateUserAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny, ]


class SignInGoogleAPIView(generics.GenericAPIView):
    serializer_class = GoogleSerializer
    permission_classes = [AllowAny, ]

    def post(self, request):
        payload = {'access_token': request.data['token']}
        r = requests.get('https://www.googleapis.com/oauth2/v2/userinfo', params=payload)
        data = json.loads(r.text)
        if 'error' in data:
            content = {'message': 'incorrect access token data'}
            return Response(content)
        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            user = User()
            name = data['email']
            user.username = name[:name.find('@')]
            user.password = make_password(BaseUserManager().make_random_password())
            user.email = data['email']
            user.save()

        token = RefreshToken.for_user(user)
        response_user = {}
        response_user['username'] = user.username
        response_user['email'] = user.email
        response_user['access_token'] = str(token.access_token)
        response_user['refresh_token'] = str(token)
        return Response(response_user)


class CityFilterViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CityFilterSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country', ]
    permission_classes = [permissions.IsAuthenticated, ]


class CityFilterAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = FilterCitySerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        self.queryset = self.queryset.filter(country_id=self.request.query_params.get('country'))
        return self.queryset


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [permissions.IsAuthenticated, ]


class CountryAPIView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated, ]


class CountryDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryDetailSerializer
    permission_classes = [permissions.IsAuthenticated, ]


class CountryCreateAPIView(generics.CreateAPIView):
    serializer_class = CountryDetailSerializer
    permission_classes = [permissions.IsAuthenticated, ]


class CountryDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Country.objects.filter()
    serializer_class = CountryDetailSerializer
    permission_classes = [permissions.IsAuthenticated, ]
