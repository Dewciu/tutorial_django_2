from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    my_context = {
        "phone_number": "530486405",
        "city"        : "Ruda Slaska",
        "street"      : "Fiołków",
        "days"        : ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    }

    return render(request, "contact.html", my_context)

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

def social_view(request, *args, **kwargs):
   

    return render(request, "social.html", {})

