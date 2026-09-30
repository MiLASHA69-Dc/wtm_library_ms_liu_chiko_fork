from django.urls import path
from .views import display_genre,delete_genre

app_name= "genres"
urlpatterns =[
    path("display-genre/",display_genre,name="display_genre"),
    path("delete-genre/<str:pk>/",delete_genre,name="delete_genre"),
]