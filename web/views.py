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
        drone = Drone.objects.get(user=self.request.user)
        drone.active,drone.roll,drone.pitch,drone.yaw,drone.throttle = False,0,0,0,0
        drone.save()
        logout(request)
        return redirect(reverse('signin'))



class dash(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def get(self, request):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        return render(request,'web/index.html')



class connect(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def post(self,request):
        drone = Drone.objects.get(user=self.request.user)
        drone.active = True
        drone.save()
        return Response({'status' : 200})




class update(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def post(self,request):
        drone = Drone.objects.get(user=self.request.user)
        drone.roll,drone.pitch,drone.yaw,drone.throttle=request.data['roll'],request.data['pitch'],request.data['yaw'],request.data['throttle']
        drone.save()
        return Response({'status' : 200})


class getData(APIView):
    def get(self,request,*args,**kwargs):
        drone = Drone.objects.get(pk=self.kwargs['id'])
        response = {
            'roll' : drone.roll,
            'pitch' : drone.pitch,
            'yaw'   : drone.yaw,
            'throttle' : drone.throttle,
            'active' : drone.active
        }

        return Response(response)
