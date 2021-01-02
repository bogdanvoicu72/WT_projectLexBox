from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.



def Avocat_View(request):

    if request.method == 'GET':
        msg = "S-a apelat Ajax-ul"
        return HttpResponse("Succes")

    return  render(request,'./AvocatView/Avocat_View.html')