from django.shortcuts import render
# from django.contrib.auth.models import User


def homepage(request):
    
    return render(request, 'home.html')

# def homepage(request):
#     context = {
#         'users' : User.objects.all()
#     }
#     return render(request, 'home.html', context)