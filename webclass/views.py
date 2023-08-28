from django.shortcuts import render
from django.http import HttpResponse
#from .import models
from .models import  Product, Signin, Contactus
from .forms import ContactForm, SigninForm, ContactusForm

# Create your views here.
def home (request):
    # num = 1
    # num_2 = 4
    # sum = num + num_2

    return HttpResponse("hellow")

def Contact(request):

    product =Product.objects.all()
    contactForm = ContactForm()

    context = {
       "products":product,
       "contactForm": contactForm
    }
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

    return render(request,"contact.html", context )


def Index4(request):
    return render(request, "index4.html")

def Rooms(request):
    return render(request, "rooms.html")

def Logout(request):
    return render(request, "logout.html")


def Admin_add_amenities(request):
    return render(request, "admin_add_amenities.html")

def Dining(request):
    return render(request, "dining.html")

def Events(request):
    return render(request, "events.html")

def Gallery(request):
    return render(request, "gallery.html")

def signin(request):

    signin = Signin.objects.all()
    signinForm = SigninForm()

    context = {
        "signins": signin,
        "signinForm": signinForm
    }
    if request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    
    return render(request, "sign_in.html", context)

def contactus(request):

    contactus = Contactus.objects.all()
    contactusForm = ContactusForm()

    context ={
        "contactuse": contactus,
        "contactusForm": contactusForm

    }
    if request.method == "POST":
        form = ContactusForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

    return render(request, "contactus.html", context)
