from django.urls import path
from .views import homePage, details, sign_in, logout_command, sign_up

urlpatterns = [
    path('', homePage, name='home_url'),
    path('details/<int:pk>/', details, name='details_url'),
    path('authenticate/', sign_in, name='login_url'),
    path('logout/',logout_command, name='logout_url'),
    path('sign_up/',sign_up, name='signup_url'),
]
