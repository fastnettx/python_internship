from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import City, Country, Symbol
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm


def base(request):
    return render(request, 'base.html')


@login_required(login_url='/login/')
def list_of_counries(request):
    list_counries = Country.objects.all()
    flag = Symbol.objects.all()
    return render(request, 'locations/list_of_counries.html', {'list_counries': list_counries, 'flag': flag})


@login_required(login_url='/login/')
def show_the_city(request, country_id):
    country = get_object_or_404(Country, id=country_id)
    city = City.objects.filter(country_id=country_id)

    if request.method == 'POST':
        city_delete = City.objects.get(id=request.POST['city_name'])
        city_delete.delete()
    return render(request, 'locations/country.html', {'country': country, 'city': city})


@login_required(login_url='/login/')
def details_city(request, country_id, city_id):
    city = get_object_or_404(City, id=city_id)
    country_city = get_object_or_404(Country, id=country_id)
    return render(request, 'locations/city.html', {'city': city, 'country': country_city})


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # страница редиректа после регистрации
    else:
        form = UserCreationForm()
    return render(request, 'registration/sign_up.html', {'form': form})
