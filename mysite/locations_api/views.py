from requests import Response
from rest_framework import viewsets, permissions, generics, status
from .serializers import (CountrySerializer, CitySerializer, CityFilterSerializer, CountryDetailSerializer,
                          TestFiltersSerializer)
from django_filters.rest_framework import DjangoFilterBackend
from locations.models import Country, City


class CityFilterSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CityFilterSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country', ]
    permission_classes = (permissions.IsAuthenticated,)


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (permissions.IsAuthenticated,)


class CountryViewSet(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDetailViewSet(generics.RetrieveUpdateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryDetailSerializer


class CountryCreateAPIView(generics.CreateAPIView):
    serializer_class = CountryDetailSerializer


class CountryDelete(generics.RetrieveDestroyAPIView):
    queryset = Country.objects.filter()
    serializer_class = CountryDetailSerializer


# Need help implementing
class CityFilterTest(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = TestFiltersSerializer

    # Failed to implement custom filter by overriding the built-in method: get_queryset()
    # def get_queryset(self):
    #     queryset = self.queryset
    #     country = self.request.query_params.get('country')
    #     if country:
    #         queryset = queryset.filter(country_id=country)
    #     return queryset

    # Failed to implement custom filter by overriding the built-in method: get()
    # def get(self, request):
    #     query_serializer = TestFiltersSerializer(data=self.request.query_params)
    #     query_serializer.is_valid(raise_exception=True)
    #     self.queryset = self.queryset.filter(country_id=query_serializer.data.get('country'))
    #     serializer = CitySerializer(self.queryset, many=True)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
