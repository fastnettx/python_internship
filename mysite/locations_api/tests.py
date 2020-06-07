from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from locations.models import Country, City, Symbol


class LocationsApiTests(APITestCase):
    def setUp(self):
        Symbol.objects.create(id=1,
                              image="smile.jpg")
        Symbol.objects.create(id=2,
                              image="f6.png")
        Country.objects.create(id=1,
                               name='TestName',
                               description='TestDescription',
                               population=100,
                               cities_count=100,
                               flag_id=1
                               )
        City.objects.create(id=1,
                            name='TestCity',
                            country_id=1,
                            longitude=222,
                            latitude=222)
        self.user_test = User.objects.create_user(username='test', password='452qwE14')
        self.user_test.save()
        self.user_test_token = Token.objects.create(user=self.user_test)
        self.client.credentials(HTTP_AUTORIZATION='Token ' + self.user_test_token.key)
        self.client.force_authenticate(user=self.user_test, token=self.user_test_token.key)

    def test_list_of_country(self):
        url = reverse('list_of_country')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_country_create(self):
        url = reverse('country_create')
        data = {
            "name": "TestName2",
            "description": "TestDescription2",
            "population": 5,
            "cities_count": 5,
            "flag": 2
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Country.objects.count(), 2)

    def test_country_change(self):
        url = reverse('country_change', kwargs={'pk': 1})
        response = self.client.patch(url, {"name": "TestNameNew"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_country_delete(self):
        url = reverse('country_delete', kwargs={'pk': 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_of_city(self):
        url = reverse('list_of_city-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_city_create(self):
        url = reverse('list_of_city-list')
        data = {'name': 'TestCity2',
                'country': 1,
                'longitude': 3,
                'latitude': 3
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(City.objects.count(), 2)

    def test_city_change(self):
        url = reverse('list_of_city-detail', args=[1])
        response = self.client.patch(url, {"name": "TestCityNew"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_city_delete(self):
        url = reverse('list_of_city-detail', args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
