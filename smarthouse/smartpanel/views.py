# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse
import paho.mqtt.client as mqtt
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from models import device, devicelog

# Create your views here.

@csrf_exempt
def loginview(request):
    if request.is_ajax():
        username = request.POST.get('username')
        password = request.POST.get('password')
        userObj = authenticate(username= username,password= password)
        if userObj is not None:
            login(request,userObj)
            responce = HttpResponse("OK")
        else:
            responce = HttpResponse("Wrong Credentials")
    else:
        responce = render(request,'index.html',context={})
    return responce


def home(request):
    user = request.user
    if user is not None:
        deviceObj = device.objects.get(user_id= user)
        deviceLogObj = devicelog.objects.filter(device=deviceObj)

        responce = render(request, 'home.html', context={"user":user,"device":deviceObj,"devicelog":deviceLogObj})
    else:
        responce = HttpResponse('Not Valid ')
    return responce


@csrf_exempt
def asyncupdation(request,device_id):
    if request.method == "POST":
        temp = request.POST.get('temp')
        humi = request.POST.get('humi')
        moist = request.POST.get('moist')
        wp = request.POST.get('wp')
        fn = request.POST.get('fn')
        ht = request.POST.get('ht')
        deviceObj =  device.objects.get(device_uid=device_id)
        deviceLogObj = devicelog(device=deviceObj,temperature=temp,humidity=humi,moisture=moist,waterpump=wp,fan=fn,heater=ht)
        deviceLogObj.save()
        return HttpResponse('Ok')
    return HttpResponse('Not Post')




@csrf_exempt
def registerview(requets):
    if requets.is_ajax():
        Name = requets.POST.get('name')
        Email = requets.POST.get('email')
        userObj = User(first_name=Name,username=Email,email=Email)
        userObj.set_password("Testing123")
        userObj.save()
        deviceObj = device(user_id=userObj)
        deviceObj.save()
        deviceLogObj = devicelog(device=deviceObj)
        deviceLogObj.save()
        return HttpResponse("Ok")
    return render(requets,'register.html',context={})


def slogout(request):
    logout(request)
    return HttpResponse("Logout Successfully")
