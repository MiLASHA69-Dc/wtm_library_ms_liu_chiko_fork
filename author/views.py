from django.shortcuts import render, redirect
from django.http import HttpResponse
# to have to my database, Import models module
from .models import Author
from .forms import CreateAuthorEntry
# Create your views here.

def author_view(request):
    # return HttpResponse("<h2>This is a registered Author Application</h2> <strong>Yeay our first application in Django under development </strong>")
    all_author = Author.objects.all().order_by("-id")
    return render(request,"author/display_author.html",{"display_all_author":all_author})

def author_entry(request):
    if request.method == "POST":
        author_form = CreateAuthorEntry(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect("display_authors")

    else:
        author_form = CreateAuthorEntry()

    context ={
        "create_form":author_form
    }
    return render(request,"author/create_author.html",context)

