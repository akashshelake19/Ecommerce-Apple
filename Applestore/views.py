from django.shortcuts import render

# Create your views here.
def Home(r):
    return render(r,'Applestore/Home.Html')