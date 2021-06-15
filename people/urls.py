from django.urls import path
from people import views as people_views

app_name = "people"

urlpatterns = [
    path("", people_views.PeopleView.as_view(), name="people"),
    path("<int:pk>", people_views.PeopleDetail.as_view(), name="detail"),
    path("<int:pk>/edit/", people_views.UpdatePeopleView.as_view(), name="edit"),
    path("create", people_views.CreatePeopleView.as_view(), name="create"),
]
