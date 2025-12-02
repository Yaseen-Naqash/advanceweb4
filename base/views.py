from django.shortcuts import render
from .models import Product
# Create your views here.

def homePage(request):
    products = Product.objects.all()
    context = {

        'products':products,
    }

    return render(request, 'index.html', context)


def details(request):
    return render(request, 'single.html')