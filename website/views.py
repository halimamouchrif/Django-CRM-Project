from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm, AddCustomerForm
from .models import Record

def home(request):
    records = Record.objects.all()
    #check if user is authenticated
    if request.method == 'POST':
        username =request.POST['username']
        password =request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in, please retry...")
            return redirect('home')
    else: 
        return render(request, 'home.html',{'records':records})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #Authentication and login

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "You have been registered!")
            return redirect('home')
    else:
        form = RegisterForm()
        return render(request, 'register.html',{'form': form})
    
    return render(request, 'register.html',{'form': form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'customer_record.html',{'customer': customer_record})
    else:
        messages.success(request, "You must be logged in!")
        return redirect('home')
    
def customer_delete(request,pk):
    if request.user.is_authenticated:
        customer_record_to_delete = Record.objects.get(id=pk)
        customer_record_to_delete.delete()
        messages.success(request, "Record deleted successfully!")
        return redirect('home')    
    else: 
        messages.success(request, "You must be logged in!")
        return redirect('home')
def customer_add(request):
    form =AddCustomerForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "A new customer added!")
                return redirect('home')
        return render(request, 'customer_add.html', {'form':form})
    else:
        messages.success(request, "You must be logged in!")
        return redirect('home')

def customer_update(request, pk):
    if request.user.is_authenticated:
        customer_record_to_update = Record.objects.get(id=pk)
        form =AddCustomerForm(request.POST or None, instance=customer_record_to_update)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully!")
            return redirect('home')
        return render(request, 'customer_update.html', {'form':form})
    else: 
        messages.success(request, "You must be logged in!")
        return redirect('home')