from django.shortcuts import render

# Create your views here.
def home2(request):
    return render(request,"home2.html")
def generate(request):
    return render(request,"generate.html")
def wishlist(request):
    return render(request,"wishlist.html")
