from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Userprofile
from store.forms import ProductForm
from store.models import Products

# Create your views here.

@login_required
def my_vendor(request):
    products = request.user.products.exclude(status=Products.DELETED)
    return render(request, 'profiles/myvendor.html', {'products': products})

@login_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            title = request.POST.get("title")

            product = form.save(commit=False)
            product.user = request.user
            product.slug = slugify(title)
            product.save()

            messages.success(request, 'Your Product Was Added Successfully')

            return redirect('myvendor')
    else:
        form = ProductForm()
    
    return render(request, 'profiles/add_product.html', {'title': 'Add Product', 'form': form})


@login_required
def edit_product(request, pk):
    product = Products.objects.filter(user=request.user).get(pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid:
            form.save()

            messages.success(request, 'Your Changes was saved!')

            return redirect('myvendor')

    else:
        form = ProductForm(instance=product)

    return render(request, 'profiles/add_product.html', {
        'title': 'Edit Product', 
        'product': product, 
        'form': form
        })

@login_required
def delete_product(request, pk):
    product = Products.objects.filter(user=request.user).get(pk=pk)
    product.status = Products.DELETED
    product.save()

    messages.success(request, 'Your product was deleted')

    return redirect('myvendor')

def vendor_detail(request, pk):
    user = User.objects.get(pk=pk)
    products = user.products.filter(status=Products.ACTIVE)

    return render(request, 'profiles/vendor_detail.html', {'user': user, 'products': products})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            user_profile = Userprofile.objects.create(user=user)

            return redirect('frontpage')
    else:
        form = UserCreationForm()

    return render(request, 'profiles/signup.html', {'form': form})

@login_required
def myaccount(request):
    return render(request, 'profiles/myaccount.html', {})