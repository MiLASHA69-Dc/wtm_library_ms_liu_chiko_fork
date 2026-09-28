from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def author_view(request):
    return HttpResponse("<h2>This is a registered Author Application</h2> <strong>Yeay our first application in Django under development </strong>")