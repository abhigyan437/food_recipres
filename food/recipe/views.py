from django.shortcuts import render, redirect
from .models import Recipes,Users

def home(request):
    return render(request,'login.html')

def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        try:
            mem = Users.objects.filter(name = name).values()
            if mem[0]['password'] == password:
                return redirect('recipe_list')
            else:
                return render(request, 'error_login.html')
        except:
            return render(request, 'error_login.html')
    else:
        return render(request,'error_login.html')


def register(request):
    return render(request,'register.html')

def registering(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        a = Users(name = name,password = password)
        a.save()
        return redirect('recipe_list')

def register_login(request):
    return redirect('login')

def recipes_page(request):
    names = Recipes.objects.all().values()
    return render(request,'recipe_list.html',{'list1':names})

def add(request):
    return render(request,'add_recipe.html')

def adding(request):
    if request.method == 'POST':
        name = request.POST.get('recipe_name')
        desc = request.POST.get('recipe_desc')
        mem = Recipes(recipe_name = name, recipe_description = desc)
        mem.save()
    return redirect('recipe_list')

def individual_page(request,recipe_name):
    value = Recipes.objects.get(recipe_name = recipe_name)
    return render(request,'recipe_page.html',{'value':value})

