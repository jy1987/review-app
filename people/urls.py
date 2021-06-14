from django.urls import path
from people import views as people_views

app_name = "people"

urlpatterns = [
    path("", people_views.PeopleView.as_view(), name="people"),
    path("<int:pk>", people_views.PeopleDetail.as_view(), name="detail"),
]
