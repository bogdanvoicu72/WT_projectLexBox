from django.shortcuts import render, redirect
from django.http import HttpResponse
import pymongo

# Create your views here.



def Avocat_View(request):

    if request.method == 'GET' and  request.GET.get('req') == '':
        client = pymongo.MongoClient("mongodb+srv://avocat:ferari99@cluster0.zfhsj.mongodb.net/Test?retryWrites=true&w=majority")
        db = client.get_database('Test')
        collection = 'InfoAvocat'
        query_collection = db[collection]
        #for x in query_collection.find({"_id":1,"Info": 1}):
           # print(x)
        x = query_collection.find_one({"_id": "5ff1a80deb286a95d728eb8c"})
        print(x)




    return  render(request,'./AvocatView/Avocat_View.html')