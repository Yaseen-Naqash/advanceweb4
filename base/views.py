from django.shortcuts import render, redirect
from .models import Product, Person
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages

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

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_url')
        else:
            messages.error(request, 'username or password is incorrect')
            return redirect('login_url')
    
    return render(request, 'login.html')

def sign_up(request):



    user = Person.objects.create(

    )
    s
    return


def logout_command(request):
    logout(request)
    return redirect('home_url')



# login
# logout
# authenticate