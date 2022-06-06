# from django.http import HttpResponse
from django.shortcuts import render

context = {
    'name': 'Easy',
}


def home(request):
    return render(request, 'recipes/pages/home.html', context=context)
