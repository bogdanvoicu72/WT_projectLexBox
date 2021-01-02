from django.urls import path
from LexBoxAvocat import views



urlpatterns = [

        path('Avocat_View',views.Avocat_View, name = 'Avocat_View')
]