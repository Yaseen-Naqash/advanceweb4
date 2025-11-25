from django.urls import path
from .views import homePage, details

urlpatterns = [
    path('', homePage, name='home_url'),
    path('details/', details, name='details_url')
    
]
