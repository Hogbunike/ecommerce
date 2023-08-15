from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Userprofile
# Create your views here.

def vendor_detail(request, pk):
    user = User.objects.get(pk=pk)

    return render(request, 'profiles/vendor_detail.html', {'user': user})

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

def myaccount(request):
    return render(request, 'profiles/myaccount.html', {})