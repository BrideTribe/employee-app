from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.forms import UserUpdateForm
from users.models import CustomUser
from profiles.forms import ProfileUpdateForm
from django.contrib import messages

# Create your views here.

@login_required
def profile(request, pk):
    profile1 = CustomUser.objects.get(id = pk)
    return render(request, 'profiles/profile.html', { 'profile1': profile1 })

@login_required
def profile_edit(request):
    if request.method == "POST":
        # u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        # if u_form.is_valid() and p_form.is_valid():
        if p_form.is_valid():
            # u_form.save()
            p_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect('profiles:profile')
    else:
        # u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
    context = {
        # 'u_form': u_form,
        'p_form': p_form
    }
    
    return render(request, 'profiles/profile_edit.html', context)
