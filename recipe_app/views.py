from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
import requests
from .models import Recipe
# Create your views here.

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'
    context_object_name = 'recipes'

    def post(self, request):
        ingredients = request.POST.get('ingredients', '')
        url = 'https://api.spoonacular.com/recipes/findByIngredients'
        params = {
            'ingredients': ingredients,
            'apiKey': '8f8392c4ccf64cd7a49eec8e2d91b099',
        }
        response = requests.get(url, params=params)
        if response.ok:
            recipes = response.json()
            return render(request, 'recipe_list.html', {'recipes': recipes})
        return render(request, 'recipe_list.html')



class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = self.object  # get the recipe object
        api_key = '8f8392c4ccf64cd7a49eec8e2d91b099'
        url = f'https://api.spoonacular.com/recipes/{recipe.id}/information?apiKey={api_key}'
        response = requests.get(url)
        data = response.json()
        context['recipe_data'] = data  # add recipe data to context
        return context