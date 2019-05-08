from django.shortcuts import render, get_object_or_404
from .models import Root, Test


def home(request):
    roots = Root.objects
    return render(request, "dictionary/home.html", {'roots': roots})


def test(request):
    roots = Root.objects
    return render(request, "dictionary/test.html", {'roots': roots})


def details(request, root_id):
    rootdetail = get_object_or_404(Root, pk=root_id)
    return render(request, "dictionary/root.html", {"root": rootdetail})



