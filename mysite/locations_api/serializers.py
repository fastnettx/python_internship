from django.contrib.auth.models import User, Group
from rest_framework import serializers
from locations.models import Country


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'is_superuser', 'email']


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ['name', 'description', 'population']
