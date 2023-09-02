from django import forms

from .models import Products, Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'address', 'zip_code', 'city',)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('category', 'title', 'description', 'price', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': 'px-7 border border-gray-200'
            }),
            'title': forms.TextInput(attrs={
                'class': ' w-full px-4 border border-gray-200'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-4 border border-gray-200'
            }),
            'price': forms.TextInput(attrs={
                'class': 'w-full px-4 border border-gray-200'
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full px-4 border border-gray-200'
            }),
        }