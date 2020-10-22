from django.shortcuts import render
import templates
# Create your views here.


def home(request):
    
    return render(request,'home.html')



def gunoi(request):

    return render(request, 'Gunoi.html')


def parcare(request):

    return render(request, 'Parcare.html')