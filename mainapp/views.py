from django.shortcuts import render
from .forms import userregistrationform
from .forms import registrationform
def index(request):
    #if request.method=="GET"
    #fm=user()
    return render(request,"index.html")

# def index(request):
#     return render("index.html")

#def indconex(request):
 #   return render(request,"contactus.html")

def registration(request):
    fm=userregistrationform()
    fm1=registrationform()
    return render(request,"registration.html",{"form":fm,"form1":fm1})