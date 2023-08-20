from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 

urlpatterns = [
    path('vendors/<int:pk>/', views.vendor_detail, name='vendor_detail'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='profiles/login.html'), name='login'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('myvendor/', views.my_vendor, name='myvendor'),
    path('edit_product/<int:pk>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),
    path('add_product', views.add_product, name='add_product'),
    
]