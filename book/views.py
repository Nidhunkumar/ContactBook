from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import ContactsCrationForm
from .models import Contact_details
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    return render(request,"index.html")

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("index")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request,"login.html", context={"login_form":form})

def user_registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            
            messages.success(request, "Registration successful." )
            return redirect("user-login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = UserCreationForm()
    return render (request, "register.html", context={"register_form":form})

@login_required
def logout_request(request):
    logout(request)
    return redirect("index")     

@login_required
def contact_creation_view(request):
    if request.method =="POST":
        form=ContactsCrationForm(request.POST)
        if form.is_valid():
            contacts=form.save(commit=False)
            contacts.user=request.user
            contacts.save()
            messages.success(request,f"contact successfully added")
            return redirect("index")
    form=ContactsCrationForm()
    return render(request,"add_contacts.html",context={"contact_form":form})

@login_required
def all_contacts_view(request):
    contacts=Contact_details.objects.filter(user=request.user)
    return render(request,"all_contacts.html",context={"contacts":contacts})


@login_required
def contact_update_view(request,id):
    contact=get_object_or_404(Contact_details,id=id)
    if request.method == "POST":
        form=ContactsCrationForm(request.POST,instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request,f"contact updated successful")
            return redirect("all-contacts")
    else:
        form=ContactsCrationForm(instance=contact)
    return render(request,"contacts_update.html",context={"contacts":form})


@login_required
def contact_delete_view(request,id):
    contact=get_object_or_404(Contact_details,id=id)
    contact.delete()
    messages.success(request,f"{contact.name} has been deleted")
    return redirect("all-contacts")

    