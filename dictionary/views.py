from django.shortcuts import render
from .models import Word


def home(request):
    words = Word.objects
    return render(request, "dictionary/home.html", {'words': words})

