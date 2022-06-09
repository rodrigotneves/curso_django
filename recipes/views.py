# from django.http import HttpResponse
from django.shortcuts import render

home_context = {
    'name': 'Easy Recipes',
    'title': 'Home',
}

recipe_context = {
    'name': 'Easy Recipes',
    'title': 'Receita',
}


def home(request):
    return render(request,
                  'recipes/pages/home.html',
                  context=home_context)


def recipe(request, id):
    return render(request,
                  'recipes/pages/recipe-view.html',
                  context=recipe_context)
