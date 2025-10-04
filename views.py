from django.shortcuts import render
from myapp.models import *

# Create your views here.
def Departmentpage(request):
    
    return render(request,"departmentpage.html")


def basepage(request):
    return render(request,"base.html")


def employeepage(request):
 
    return render(request,"employeepage.html")

def basicinfopage(request):
    
    return render(request,"basicinfopage.html")
