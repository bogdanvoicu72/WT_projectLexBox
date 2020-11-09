from django.shortcuts import render
import templates
# Create your views here.


def home(request):
    
    return render(request,'home.html')



def cerere(request):

    return render(request, 'Cerere.html')


def parcare(request):

    return render(request, 'Parcare.html')