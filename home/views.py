from django.shortcuts import render
from django.views import View
# Create your views here.

def landing_page(request):
    return render(request, 'landing_page.html')

