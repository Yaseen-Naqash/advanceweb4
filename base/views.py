from django.shortcuts import render, redirect
from .models import Product, Person
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth.decorators import login_required



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

@login_required
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
    if request.method == 'POST':
        username = request.POST.get('username')
        fullname = request.POST.get('fullname')
        confirmpassword = request.POST.get('password2')
        password = request.POST.get('password1')
        image = request.FILES.get('image')
        if password != confirmpassword:
            messages.error(request, 'your password does not match!')
            return redirect('logni_url')
        try:
            Person.objects.get(username=username)
            messages.error(request, 'username already taken')
            return redirect('login_url')
        except Person.DoesNotExist:
            user = Person.objects.create(
                username=username,
                first_name = fullname,
                profile_image = image   
            )
            user.set_password(confirmpassword)
            user.save()
            pass


    messages.success(request, 'your account created succsessfully')
    return redirect('login_url')


def logout_command(request):
    logout(request)
    return redirect('home_url')



# login
# logout
# authenticate