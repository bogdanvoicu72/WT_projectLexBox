from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from LEXBOX.settings import EMAIL_HOST_USER
from docxtpl import DocxTemplate
from django.contrib.staticfiles.storage import staticfiles_storage

import requests
import json
from config import REST_API_URL

template_location = staticfiles_storage.path('Plangere.docx')


def home(request):
    return render(request, 'home.html')


# Be sure to run `python3 manage.py collectstatic`
# or whatever's the command on your machine
# before running this.

def cerere(request):
    # if request.POST:
    if request.method == "POST":
        request_file = request.FILES['document'] if 'document' in request.FILES else None
        if request_file:
            fs = FileSystemStorage()
            fs.save(request_file.name, request_file)

        doc = DocxTemplate(template_location)
        doc.render(request.POST)
        doc.save("generated_doc.docx")
        # Doamna avocat va primi un mail de notificare cand se va completa o noua cerere
        subject = "Ati primit o cerere noua"
        # message = "O noua cerere a fost adougata in contul dumneavoastra!"
        message = "<b>TEXT INPUTS:</b> \n\n"
        message += "\n".join(str(request.POST).split(","))
        message += "\n\n<b>FILE INPUTS:</b>\n\n"
        message += "\n".join(str(request.FILES).split(","))

        receipents = ["dan.tomoiu99@e-uvt.ro", "dodov1999@gmail.com", "iulia.hurloi99@e-uvt.ro"]

        # uploaded_file = request.FILES['file'] # file is the name value which you have provided in form for file field

        for recepient in receipents:
            # send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently=False)
            pass

        request_data = json.dumps(request.POST)
        req = requests.post(REST_API_URL, json=request_data)

        print("from request: " + str(req))

        return render(request, 'success_request.html', context={'data': request.POST})
    else:
        return render(request, 'wizard.html')


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
            login(request, user)
            return redirect('login')
        else:
            form = UserCreationForm()
    return render(request, 'avo.html', {'form': form})


def info_avo(request):
    return render(request, 'info_avo.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('info_avo')

    return render(request, 'login.html')


def user_page(request):
    return render(request, 'user_page.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_page')

    return render(request, 'user_login.html')


def user_singin(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
        else:
            form = UserCreationForm()
    return render(request, 'user_singin.html', {'form': form})
