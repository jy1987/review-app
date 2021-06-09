from django.urls import path
from books import views as books_views

app_name = "books"

urlpatterns = [path("", books_views.all_books, name="books")]
