from multiprocessing import context
from tkinter.tix import Form
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Lib
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from .forms import ContactUsForm


# Create your views here.


# Landing page view
def index(request):
    animation_objects = Lib.objects.all()
    animation_types = []
    for animation in animation_objects:
        if animation.anima_type not in animation_types:
            animation_types.append(animation.anima_type) 
    paginator = Paginator(animation_types,8)
    page = request.GET.get('page') 
    animation_types = paginator.get_page(page)  
    context = {
        'animation_types': animation_types,
        'animation_objects': animation_objects        
    } 
    return render(request, 'accounts/index.html', context) 


# Registration view
def register(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == 'POST': 
        form = RegisterForm(request.POST) 
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                messages.error(request, f'The email {email} already exists!')
                return redirect('accounts:register') 
            form.save()                              
            messages.success(request, f'Welcome {username}, your account is created.')            
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form':form})


# Profile page view
@login_required
def profilepage(request):
    return render(request, 'accounts/profile.html')

#ContactUs Page View

@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST, instance=User) 
        if form.is_valid():
            form.save()
    
    return render(request, 'accounts/contact.html')

# def contact(request, pk):
#     user = User.objects.get(id=pk)
#     form = ContactUsForm()
#     if request.method == 'POST':
#         form = ContactUsForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             # return redirect('accounts/contact.html')
#     return render(request, 'accounts/contact.html', {'form': form})


# def createOrder(request, pk):
    
#     customer = Customer.objects.get(id=pk)
#     formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
#     if request.method == 'POST':
#         form = OrderFormSet(request.POST, instance=customer)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     context = {'formset': formset}
#     return render(request, 'accounts/order_form.html', context)









# @login_required
# def contact(request):
#     form_class = ContactUsForm
#     # if request is not post, initialize an empty form
#     form = form_class(request.POST or None)
#     if request.method == 'POST':
#         form = form_class(request.POST)
#         if form.is_valid():
#             user= form.cleaned_data.get('user')
#             email = form.cleaned_data.get('email')
#             if User.objects.filter(email=email).exists():
#                 messages.error(request, f'{email} does not seem to be registered with us!')
                
#                 return render(request, 'contact.html', {'form': form})
#             else:   
#                 form.save()
#                 messages.success(request, f'Thank you {user}, we have received your message!')
#                 redirect('contact.html')
#     else: 
#         return render(request, 'accounts/contact.html')
    
            