from django.urls import path
from LEXBOXapp import views



urlpatterns = [
    path('', views.home),
    path('Gunoi', views.gunoi),
    path('Parcare',views.parcare),
]