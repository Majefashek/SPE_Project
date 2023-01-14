from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegisterUserForm,PostForm
from django.contrib import messages
from .models import Post,Jobs,CustomUser
from django.contrib.auth.models import User

def add_image(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)  # This will print the form errors to the console
    else:
        form = PostForm()
    return render(request, 'SPE_webapp/add_image.html', {'form': form})

jobs = Jobs.objects.all()
 

def Jobs(request):
	

    if request.user.is_authenticated and request.user.is_admin:
        return render(request, 'SPE_webapp/Jobs.html', {'jobs': jobs})
    else:
        return render(request,'SPE_webapp/myjobs.html',{'jobs':jobs})



	


def home(request):

	users=CustomUser.objects.all()
	
	return render(request,'SPE_webapp/home.html',{'users':users})


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

	return render(request, 'SPE_webapp/register_user.html', {
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
		return render(request,"SPE_webapp/index.html")	





