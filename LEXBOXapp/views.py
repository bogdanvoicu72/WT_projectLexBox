from bson import ObjectId
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from LEXBOX.settings import EMAIL_HOST_USER
from docxtpl import DocxTemplate
from django.contrib.staticfiles.storage import staticfiles_storage
import pymongo
from .forms import SignUpForm
import requests
import json
from config import REST_API_URL

template_location = staticfiles_storage.path('Plangere.docx')


def home(request):
    return render(request, 'home.html')


# Be sure to run `python3 manage.py collectstatic`
# or whatever's the command on your machine
# before running this.

#doc = DocxTemplate(template_location)
#doc.render(request.POST)
#doc.save("generated_doc.docx")
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
    #request.post('http://127.0.0.1:5000/generate_document',request.POST ,json=json.dumps(request.post,indent=4))

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
        print(request_data)
        #print("from request: " + str(req))

        return render(request, 'success_request.html', context={'data': request.POST})
    else:
        return render(request, 'wizard.html')


def parcare(request):
    return render(request, 'Parcare.html')


def avo(request):    #Avocat Register
    if request.method ==  'POST':
        requests.post('http://127.0.0.1:5000/register_avocat', json = json.dumps(request.POST))
    return render(request, 'avo.html')


#def info_avo(request):

   # if request.method == 'GET' and request.POST.get('req') == '':
      #  print("intra in if")
      #  client = pymongo.MongoClient("mongodb+srv://avocat:avocat@cluster0.zfhsj.mongodb.net/Cluster0?retryWrites=true&w=majority")
      #  db = client.get_database('Cluster0')
       # collection = 'sample_mflix.movies'
        #query_collection = db[collection]
        #q = query_collection.find_one({ resource: { db: "test", collection: "" }, actions: [ "listCollections" ] })
       # print(q)
       # print("fsjahfa")




    #return render(request, 'AvocatView/Avocat_View.html')





def user_page(request):      #Pagina unde utilizatprul CONECTAT poate sa faca cerere
    return render(request, 'user_page.html')


def user_login(request):    #pagina de Login pentru avocat sau utilizator
    if request.method == 'POST':
        result = requests.post("http://127.0.0.1:5000/login", request.POST)

        if result.status_code == 200:
            return redirect('/Cerere')

    return render(request, 'user_login.html')


def user_signin(request):     #pagina de register pentru Utilizator
    if request.method == 'POST':

        result = requests.post("http://127.0.0.1:5000/register", request.POST)

    return render(request, 'user_singin.html')







