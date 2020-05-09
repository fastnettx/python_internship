from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import City, Country, Symbol
from .forms import AddCountry, AddCity, AddSymbol
from django.contrib.auth.forms import UserCreationForm


def base(request):
    return render(request, 'base.html')


@login_required(login_url='/login/')
def list_of_counries(request):
    list_counries = Country.objects.all()
    flags = Symbol.objects.all()
    return render(request, 'locations/list_of_counries.html', {'list_counries': list_counries, 'flags': flags})


@login_required(login_url='/login/')
def show_the_city(request, country_id):
    country = get_object_or_404(Country, id=country_id)
    city = City.objects.filter(country_id=country_id)

    if request.method == 'POST':
        city_delete = City.objects.get(id=request.POST['city_id'])
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
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/sign_up.html', {'form': form})


@login_required(login_url='/login/')
def add_country(request, add_country):
    if request.method == "POST":
        form = AddCountry(request.POST)
        if form.is_valid():
            # post = form.save(commit=False)
            # post.users = User.objects.get(username=request.user)
            form.save()
            return redirect('list_of_counries')
    else:
        form = AddCountry()
    return render(request, 'locations/add_country.html', {'form': form})


@login_required(login_url='/login/')
def edit_country(request, country_id):
    post = get_object_or_404(Country, id=country_id)
    if request.method == "POST":
        form = AddCountry(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('list_of_counries')
    else:
        form = AddCountry(instance=post)
    return render(request, 'locations/edit_country.html', {'form': form, "post": post})


@login_required(login_url='/login/')
def add_city(request, country_id, add_city):
    if request.method == "POST":

        form_city = AddCity(request.POST)
        if form_city.is_valid():
            post = form_city.save(commit=False)
            post.country_id = country_id
            post.save()
            return redirect('/list_of_counries/' + str(country_id))
    else:
        form_city = AddCity()
    return render(request, 'locations/add_city.html', {'form': form_city, 'country_id': country_id})


@login_required(login_url='/login/')
def edit_city(request, country_id, city_id):
    post = get_object_or_404(City, id=city_id)
    if request.method == "POST":
        form = AddCity(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/list_of_counries/' + str(country_id))
    else:
        form = AddCity(instance=post)
    return render(request, 'locations/edit_city.html', {'form': form, "post": post})


@login_required(login_url='/login/')
def upload_flag(request):
    if request.method == "POST":
        form = AddSymbol(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/list_of_counries/add_country')
    else:
        form = AddSymbol()
    return render(request, 'locations/upload_flag.html', {'form': form})
