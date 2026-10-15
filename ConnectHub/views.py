from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.http import JsonResponse
from .models import City
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Country
from .models import Post 
# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')
def register(request):
    countries = Country.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        country_id  = request.POST.get('country')
        email = request.POST.get('email')
        city_id = request.POST.get('city')
        dob = request.POST.get('dob')
        phone_number = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        context = {
            'countries': countries,
            'name': name,
            'email': email,
            'phone_number': phone_number,
            'dob': dob
        }

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, 'register.html')

        if User.objects.filter(username=email).exists():
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
   
    return render(request, 'register.html', {'countries': countries})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid email or password")
            return render(request, 'login.html')
    return render(request, 'login.html')

def load_cities(request):
    # This matches the '?country=' from your JavaScript fetch URL
    country_id = request.GET.get('country')
    
    cities = City.objects.filter(country_id=country_id).order_by('name')
    
    # This renders your HTML tags using the 'citys' spelling for your loop
    return render(request, 'cities.html', {'citys': cities})

 # or from connect.models import Post

def home(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Post.objects.create(user=request.user, content=content)
            return redirect('home')
    
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts}) # change index.html to your file name

