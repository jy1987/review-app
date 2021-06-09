from django.shortcuts import render
from . import models

# Create your views here.


def all_people(request):

    all_people = models.Person.objects.all()
    return render(request, "people/all_people.html", context={"people": all_people})
