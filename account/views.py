from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegisterUserForm
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth import get_user_model

def register_user(request):
	if request.method == "POST":
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("Registration Successful!"))
			return redirect('home')
	else:
		form = RegisterUserForm()

	return render(request, 'account/register_user.html', {
		'form':form,
		})


def login_view(request):
	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.error(request, ("There Was An Error Logging In, Try Again..."))	
			return redirect('login_view')
	else:
		return render(request,"account/index.html")

def myaccount(request):
    myid=request.user.id
    obj=CustomUser.objects.get(pk=myid)
    return render(request,"account/myaccount.html", {'obj':obj})

# Create your views here.
