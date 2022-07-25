from itertools import product
from multiprocessing import context
from pyexpat.errors import messages
from unicodedata import category
from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm

# Create your views here.
def index(request):
    return render(request, 'Home/home.html')

def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/index')
    else:
        form = RegisterForm()
    return render(request, 'registration/sign_up.html', {"form":form})
def home(request):

    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def collections(request):
    category = Category.objects.filter(status=0)
    context = {'category': category}
    return render(request, "collections.html", context)

# def item(request):
#     return render(request, "item.html")

def collectionsview(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
        products = Product.objects.filter(category__slug=slug)
        category_name = Category.objects.filter(slug=slug).first()
        context = {'products':products, 'category_name':category_name}
        return render(request, "products.html", context)
    else:
        messages.warning(request, "No Such Category Found")
        return redirect('collections')

def productview(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug=cate_slug, status=0)):
        if(Product.objects.filter(slug=prod_slug, status=0)):
            products= Product.objects.filter(slug=prod_slug, status=0).first
            context = {'products':products}
        else:
            messages.error(request, "No Such Category Found")
            return redirect('collections')
    else:
        messages.error(request, "No Such Category Found")
        return redirect('collections')
    return render(request, "item.html", context)
