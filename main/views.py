from django.shortcuts import render, redirect

# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('home')
def home_view(request):
    return render(request,'home.html')
# Costumer
def customer_login_view(request):
    return render(request,'accounts/seller/login.html')

def customer_register_view(request):
    return render(request,'accounts/seller/register.html')

def customer_forgot_pass_view(request):
    return render(request,'accounts/seller/forgot.html')
# Seller
def seller_login_view(request):
    return render(request,'accounts/costumer/login.html')

def seller_register_view(request):
    return render(request,'accounts/costumer/register.html')

def seller_forgot_pass_view(request):
    return render(request,'accounts/costumer/forgot.html')