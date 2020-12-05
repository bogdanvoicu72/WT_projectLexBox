from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from docxtpl import DocxTemplate
from django.contrib.staticfiles.storage import staticfiles_storage

template_location = staticfiles_storage.path('Plangere.docx')


# Create your views here.


def home(request):
    
    return render(request,'home.html')

# Be sure to run `python3 manage.py collectstatic`
# or whatever's the command on your machine
# before running this.

def cerere(request):
    #if request.POST:
    if request.method == "POST":
        request_file = request.FILES['document'] if 'document' in request.FILES else None
        if request_file:
                fs = FileSystemStorage()
                fs.save(request_file.name, request_file) 

        doc = DocxTemplate(template_location)
        doc.render(request.POST)
        doc.save("generated_doc.docx")
        return render(request, 'success_request.html', context={'data': request.POST})
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