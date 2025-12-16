from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.

def homePage(request):
    

    # filtered_products = Product.objects.filter(id=1)
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    products = Product.objects.filter(Q(title__icontains = q) | Q(description__icontains = q))
    

    category = request.GET.getlist('category')
    if len(category) != 0:
        products = products.filter(size__in = category)
    price = request.GET.get('price') if request.GET.get('price') != None else '1000'

    products = products.filter(price__lte = price)



    
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

