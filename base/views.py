from django.shortcuts import render
from .models import Product
# Create your views here.

def homePage(request):
    products = Product.objects.all()

    # filtered_products = Product.objects.filter(id=1)

    context = {

        'products':products,
    }

    return render(request, 'index.html', context)


def details(request):
    # product = Product.objects.get(price=87.90)
    # Product.objects.create(
    #     title = 'hello world',
    #     price = 50.00,
        
    # )

    return render(request, 'single.html')