from django.shortcuts import render

# Create your views here.

def homePage(request):

    return render(request, 'index.html')


def details(request):
    return render(request, 'single.html')