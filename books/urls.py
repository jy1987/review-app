from django.urls import path
from books import views as books_views

app_name = "books"

urlpatterns = [
    path("", books_views.BookView.as_view(), name="books"),
    path("<int:pk>", books_views.BookDetail.as_view(), name="detail"),
    path("<int:pk>/edit/", books_views.UpdateBookView.as_view(), name="edit"),
    path("create", books_views.CreateBookView.as_view(), name="create"),
    path(
        "<int:book_pk>/review/delete/<int:review_pk>",
        books_views.delete_review,
        name="review-delete",
    ),
]
