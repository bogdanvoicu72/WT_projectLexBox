from django.shortcuts import render
import templates
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.


def home(request):
    
    return render(request,'home.html')


def cerere(request):
    if request.POST:
        context = {'data': request.POST}
        return render(request, 'success_request.html', context=context)
    else:
        return render(request, 'Cerere.html')



def parcare(request):

    return render(request, 'Parcare.html')




def avo(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            redirect('login')
        else:
            form = UserCreationForm()
    return render(request,'avo.html', {'form': form})



def info_avo(request):

    return render(request, 'info_avo.html')


def login_page(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password =password)
        if user is not None:
            login(request,user)
            return redirect('info_avo')

    return render(request,'login.html')