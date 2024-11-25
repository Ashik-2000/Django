from django.urls import path
from .views import signUp, logIn, home, logOut

urlpatterns = [
    path('signup/', signUp, name="signup"),
    path('login/', logIn, name="login"),
    path('home/', home, name="home"),
    path('logout/', logOut, name="logout"),
]