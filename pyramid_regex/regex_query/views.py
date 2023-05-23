from django.shortcuts import render
from django.views.generic import TemplateView
import re

class HomePageView(TemplateView):
    template_name = "home.html"

def full_match(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        regex_querry = request.POST.get('regex_querry')
        matches = re.findall(regex_querry, text)
    else:
        matches = []
    return render(request, 'fullmatch.html', {'matches': matches})

def first_match(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        regex_querry = request.POST.get('regex_querry')
        match = re.search(regex_querry, text)
        if match:
            matches = [match.group()]
        else:
            matches = []
    else:
        matches = []
    return render(request, 'firstmatch.html', {'matches': matches})