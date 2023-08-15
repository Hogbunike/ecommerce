from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def vendor_detail(request, pk):
    user = User.objects.get(pk=pk)

    return render(request, 'profiles/vendor_detail.html', {'user': user})