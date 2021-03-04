from django.shortcuts import render
from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse, request
from rest_framework.views import APIView  
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate,logout, login
from rest_framework.permissions import IsAuthenticated
from web.forms import *


class signin(APIView):
    authentication_classes = [BasicAuthentication,SessionAuthentication]
    def get(self,request):
        
        context = {
            'form' : LoginForm()
        }
        return render(request,'web/login.html',context=context)

    def post(self,request):
        user = authenticate(username=request.POST['name'],password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect(reverse('dash'))
        else:
            context = {
                'form' : LoginForm(),
                'message' : "Invalid Credentials",
            }
            return render(request,'web/login.html',context=context)



class logoutpg(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def get(self, request):
        logout(request)
        return redirect(reverse('signin'))



class dash(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def get(self, request):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        return render(request,'web/index.html')


