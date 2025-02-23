from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name=""),
    path('update/<str:pk>/',views.updateTask,name='updateTask'),
    path('delete/<str:pk>/',views.deleteTask,name='deleteTask'),
]