from django.http import HttpResponse
from django.shortcuts import render

# TODO: use generic views for this
def home(request):
    return render(request, 'home.html')