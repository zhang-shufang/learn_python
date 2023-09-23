from pydoc_data.topics import topics
from unicodedata import name
from django.shortcuts import render

from .models import Pizza, Topping

# Create your views here.
def index(request):
    """披萨店主页"""
    return render(request, 'pizzaria_apps/index.html')

def pizzas(request):
    """显示所有披萨的页面"""
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas': pizzas}
    return render(request, 'pizzaria_apps/pizzas.html', context)

def pizza(request, pizza_id):
    """显示选定披萨及其馅料的页面"""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('name')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzaria_apps/pizza.html', context)