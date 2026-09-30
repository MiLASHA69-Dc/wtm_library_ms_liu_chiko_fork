from django.shortcuts import render, redirect
from .models import Genre
from .forms import CreateGenreForm
# Create your views here.

def display_genre(request):
    all_genre = Genre.objects.all().order_by("-id")
    if request.method == "POST":
        create_genre_form = CreateGenreForm(request.POST)
        if create_genre_form.is_valid():
            create_genre_form.save()
            return redirect("genres:display_genre")

    else:
        create_genre_form = CreateGenreForm()

    franco = {
        "display_genres":all_genre,
        "genre_form":create_genre_form
    }
    return render(request,"Genre/display_genre.html",franco)


def delete_genre(request,pk):
    get_genre = Genre.objects.get(id=pk)
    get_genre.delete()
    return redirect("genres:display_genre")
