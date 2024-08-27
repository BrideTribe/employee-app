from django.shortcuts import render, redirect
from .models import Worksite
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import forms


# Create your views here.
#request -> response

def posts_list(request):
    worksites = Worksite.objects.all().order_by('-date')
    return render(request, 'worksites/posts_list.html', { 'worksites': worksites })


@login_required(login_url='/users/login')
def posts_user_list(request):
    user = request.user
    user_posts = Worksite.objects.filter(author =request.user).order_by('-date')
    return render(request, 'worksites/post_user_list.html', { "user_posts": user_posts, "user": user})


def post_page(request, slug):
    worksite = Worksite.objects.get(slug=slug)
    return render(request, 'worksites/post_page.html', { 'worksite': worksite })

@login_required(login_url='/users/login')
def post_new(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            messages.success(request, f'Your post is successful!')
            return redirect('worksites:single-list')
    else:
        form = forms.CreatePost()
    return render(request, 'worksites/post_new.html', { 'form': form })

@login_required(login_url='/users/login')
def post_update(request):
    if request.method == 'PATCH':
        form = forms.UpdatePost(request.PATCH, request.FILES, instance=request.user)
        if form.is_valid():
            updatepost = form.save(commit=False)
            updatepost.author = request.user
            updatepost.save()
            messages.success(request, f'Your post has been updated!')
            return redirect('worksites:single-list')
    else:
        form = forms.UpdatePost(instance=request.user)
    return render(request, 'worksites/post_edit.html', { 'form': form })