#from django.conf.urls import url
from django.urls import path
from Restapi import views

urlpatterns = [
    path('home',views.home),
    path('login',views.create),
    path('success',views.success,name="success"),  
    #path('api/', views.loginList.as_view()),
]
