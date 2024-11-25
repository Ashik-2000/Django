from django.urls import path
from .views import signUp, logIn, Home, logOut

urlpatterns = [
    path('', signUp, name='signup'),
    path('login/', logIn, name='login'),
    path('home/', Home, name='home'),
    path('logout/', logOut, name='logout'),
]