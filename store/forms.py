from django import forms

from .models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('category', 'title', 'description', 'price', 'image',)