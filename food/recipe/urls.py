
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('signin/register/register/signin/',views.register_login, name = 'reglogin'),
    path('signin/',views.login,name = 'login'),
    path('signin/register/',views.register,name = 'register'),
    path('signin/register/registering/',views.registering,name = 'registering'),
    path('recipe_list',views.recipes_page,name = 'recipe_list'),
    path('recipe_list/add/',views.add,name = 'add'),
    path('recipe_list/<str:recipe_name>/', views.individual_page,name = 'individual_page'),

    path('recipe_list/add/adding/',views.adding,name = 'adding'),
]
