from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('mainapp/', include('mainapp.urls')),
]
