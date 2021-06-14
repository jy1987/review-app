from django.urls import path
from books import views as books_views

app_name = "books"

urlpatterns = [
    path("", books_views.BookView.as_view(), name="books"),
    path("<int:pk>", books_views.BookDetail.as_view(), name="detail"),
]
