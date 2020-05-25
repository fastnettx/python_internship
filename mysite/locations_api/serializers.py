from django.contrib.auth.models import User, Group
from rest_framework import serializers
from locations.models import Country, City


class CityFilterSerializer(serializers.ModelSerializer):
    country = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = City
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    country_name = serializers.StringRelatedField(many=True)

    class Meta:
        model = Country
        fields = ['id', 'name', 'description', 'country_name']


class CountryDetailSerializer(serializers.ModelSerializer):
    users = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD, read_only=True, many=True)

    class Meta:
        model = Country
        fields = '__all__'


# A class for writing your own filter for serializing an object
class TestFiltersSerializer(serializers.Serializer):
    country_id = serializers.IntegerField()
    name = serializers.CharField()
    country = serializers.CharField()
