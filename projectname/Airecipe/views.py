from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai

openai.api_key = 'your_openai_api_key'

# Temporary storage for wishlist (you may use a database model for production)
wishlist = []

def generate_recipe(request):
    if request.method == 'POST':
        ingredients = request.POST.get('ingredients')
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Create a recipe using these ingredients: {ingredients}",
            max_tokens=150
        )
        recipe = response.choices[0].text.strip()
        return JsonResponse({'recipe': recipe})
    return render(request, 'input_output.html')

def add_to_wishlist(request):
    if request.method == 'POST':
        recipe = request.POST.get('recipe')
        wishlist.append(recipe)
        return JsonResponse({'status': 'success'})

def view_wishlist(request):
    return render(request, 'wishlist.html', {'wishlist': wishlist})
