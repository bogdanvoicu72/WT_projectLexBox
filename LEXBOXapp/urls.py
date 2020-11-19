from django.urls import path
from LEXBOXapp import views



urlpatterns = [
    path('', views.home),
    path('Cerere', views.cerere),
    path('Parcare',views.parcare),
    path('avo', views.avo),
    path('info_avo', views.info_avo ,name='info_avo'),
    path('login',views.login_page, name='login'),
]