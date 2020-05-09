from django.utils.deprecation import MiddlewareMixin
from .models import Country


class GetListCountries(MiddlewareMixin):
    def process_request(self, request):
        list_countries = Country.objects.all()
        request.list_countries = list_countries
        return None
