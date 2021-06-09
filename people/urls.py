from django.urls import path
from people import views as people_views

app_name = "people"

urlpatterns = [path("", people_views.all_people, name="people")]