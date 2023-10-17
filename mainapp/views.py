from django.shortcuts import render,redirect
from django.http import HttpResponse

def home(req):
    return render(req,'login.html')

def loginTask(req):
    email=req.GET.get('email')
    password=req.GET.get('password')
    if email=="zarbadegagan@yahoo.in" and password=="123456":
        return redirect('/mainapp/dashboard')
    else:
        return redirect('/mainapp/home')

def dashboard(req):
    return render(req,'dashboard.html')

def addLeads(req):
    return render(req,'addlead.html')

def Leads(req):
    return render(req,'leads.html')

def invoice(req):
    return render(req,'invoice.html')

def addmissions(req):
    return render(req,'addmissions.html')

def migrations(req):
    return render(req,'migrations.html')

def consultency(req):
    return render(req,'consultency.html')

def institute(req):
    return render(req,'institute.html')

def newsletter(req):
    return render(req,'newsletter.html')

