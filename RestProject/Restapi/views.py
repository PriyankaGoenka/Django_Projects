from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from . import forms 
from .models import login
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import loginSerializer 
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.

def home(request):
    return HttpResponse("Hello Candidates!! Welcome to Djanjo Training!")

def create(request):
    if request.method=="POST":
        form=forms.SignIn(request.POST)
        if form.is_valid():
           try:
               form.save()
               return redirect('success') 
           except:
                print("Error saving")
    else:        
        form=forms.SignIn()
    return render(request,'myapp/login.html',{'form':form})

def success(request):
    return render(request, "myapp/success.html")

class loginViewsets(viewsets.ModelViewSet):
    queryset=models.login.objects.all()
    serializer_class=serializers.loginSerializer

#class loginList(APIView):
#    def get(self,request):
#        values=login.objects.all()
#        serializer=loginSerializer(values, many=True)
#        return Response(serializer.data)

#    def post(self, request, format=None):
#        serializer=loginSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



