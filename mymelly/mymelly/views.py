from django.http import HttpResponse
from django.shortcuts import render

def index (requets):
    context = {
        'judul':'HOME'
    }
    return render (requets,'index.html',context)
    
