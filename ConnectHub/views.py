from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import City
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Country
# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')
def register(request):
    if request.method == 'POST':
        name = request.POST.get('phone')
        country_id  = request.POST.get('country')
        email = request.POST.get('email')
        city_id = request.POST.get('city')
        dob = request.POST.get('dob')
        phone_number = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(render, 'register.html')

        if User.objects.filter(username=email).exists:
            messages.error(request, "Email already registered")
            return render(request, 'register.html')

        user = User.objects.create_user(
            username=email,
            email= email,
            password= password,
            first_name = name
        )
        user.save()
        return redirect('login')
    countries = Country.objects.all()
    return render(request, 'register.html', {'countries': countries})
def login_view(request):
    if request.method == 'POST':
        pass
    return render(request, 'login.html')

def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    
    # Make sure this points to 'cities.html'
    return render(request, 'cities.html', {'citys': cities})






def load_cities(request):
    country_id = request.GET.get('country_id')
    # Fetch cities belonging to the selected country, ordered alphabetically
    citys = City.objects.filter(country_id=country_id).order_by('name')
    
    # Convert the queryset into a list of dictionaries for JSON
    city_list = [{'id': city.id, 'name': city.name} for city in citys]
    return JsonResponse(city_list, safe=False)
