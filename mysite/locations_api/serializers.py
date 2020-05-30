from django.contrib.auth.models import User
from rest_framework import serializers
from locations.models import Country, City


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()

    class Meta(object):
        model = User
        fields = ['id', 'username', 'email',
                  'date_joined', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


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


class FilterCitySerializer(serializers.Serializer):
    name = serializers.CharField()
    country = serializers.CharField()
    country_id = serializers.IntegerField()
    longitude = serializers.FloatField()
    latitude = serializers.FloatField()


class GoogleSerializer(serializers.Serializer):
    token = serializers.CharField()
