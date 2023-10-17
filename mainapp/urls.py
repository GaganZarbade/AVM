from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('dashboard',views.dashboard),
    path('loginTask',views.loginTask),
    path('Leads',views.Leads),
    path('addLeads',views.addLeads),
    path('invoice',views.invoice),
    path('addmissions',views.addmissions),
    path('migrations',views.migrations),
    path('consultency',views.consultency),
    path('institute',views.institute),
    path('newsletter',views.newsletter),
]

