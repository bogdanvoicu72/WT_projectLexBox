from django.urls import path
from LEXBOXapp import views



urlpatterns = [
    path('', views.home),
    path('Cerere', views.cerere),
    path('Parcare',views.parcare),
]