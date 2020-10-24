from django.shortcuts import render
from .models import Product

# def index(request):
#     products = Product.objects.all()
#     return render(request, 'frontend/index.html', {'products' : products})

def login(request):
    return render(request, 'frontend/login.html')

def about(request):
    return render(request, 'frontend/about.html')

def skill(request):
    return render(request, 'frontend/skill.html')

def education(request):
    return render(request, 'frontend/education.html')

def contact(request):
    return render(request, 'frontend/contact.html')

