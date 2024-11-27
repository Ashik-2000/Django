from django.urls import path
from .views import signUp, logIn

urlpatterns = [
    path('', logIn, name='login'),
    path('signup', signUp, name='signup'),
]
