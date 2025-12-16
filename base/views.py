from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
# Create your views here.

def homePage(request):
    products = Product.objects.all()

    # filtered_products = Product.objects.filter(id=1)

    context = {

        'products':products,
    }

    return render(request, 'index.html', context)


def details(request, pk):

    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return HttpResponse("Product not found")


    context = {
        'product': product,
    }
    

    return render(request, 'single.html', context)

