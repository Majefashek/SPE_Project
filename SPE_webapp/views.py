from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegisterUserForm,PostForm
from django.contrib import messages
from .models import Jobs, Post, Comments
from post.models import likes
from django_ajax import decorators


def home(request):
    if request.user.is_authenticated:
        post = Post.objects.all()
        liked_user = likes.objects.all()
        return render(request,'SPE_webapp/home.html', {'post':post,
                                                        'liked_user': liked_user,
                                                        'user': request.user,})
    else:
        if request.method == 'POST':
            post = Post.objects.all()
            liked_user = likes.objects.all()
            return render(request,'SPE_webapp/home.html', {'post':post,'liked_user': liked_user,
                                                        'user': request.user,})
        else:
            messages.success(request, ('You are required to login in order to accesss this site'))
            return redirect('login_view')
        real
kdmkenmkknekfnkklnfklrnklnlknlknrlk


	




