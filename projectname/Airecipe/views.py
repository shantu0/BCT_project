from django.shortcuts import render
from groq import Groq
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
def home2(request):
    return render(request,"home2.html")
def generate(request):
    return render(request,"generate.html")
def wishlist(request):
    return render(request,"wishlist.html")

def recip(itemss):
    client = Groq(api_key="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")

    promt = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "you are a recipe generator from the given ingridents only"
            },
            {
                "role": "user",
                "content": f"Generate a recipe using the following ingredients: {itemss}"
            }
        ],
        
    )
    
    workout_plan = promt.choices[0].message.content
    return workout_plan

@csrf_exempt
def generate_recipe(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        items = data.get('items')

        
        recipe = recip(items)

        return JsonResponse({'recipe': recipe})
    return JsonResponse({'error': 'Invalid request'}, status=400)