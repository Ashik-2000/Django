from django.urls import path
from .views import signUp, logIn, logOut

urlpatterns = [
    path('signup/', signUp, name='signup'),
    path('', logIn, name='login'),
    path('logout/', logOut, name='logout'),
]