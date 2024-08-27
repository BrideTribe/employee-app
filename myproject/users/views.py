from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from users.models import CustomUser
# from django.contrib.auth.models import User


# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            login(request, form.save())
            return redirect('users:list')
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", { "form": form })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("worksites:list")
                # return redirect("/")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", { "form": form })

def logout_view(request):
    if request.method == "POST":
        logout(request)
        # return redirect("users/login")
        return render(request, "users/logout.html")
    
    
def users_view(request):
    users = CustomUser.objects.all().order_by('-date')
    return render(request, 'users/users_list.html', { 'users': users })

def user_page(request, pk):
    user = CustomUser.objects.get(id=pk)
    return render(request, 'user/users_list.html', { 'user': user })



