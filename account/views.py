
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegisterUserForm,Edit_userForm
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import  MyPasswordChangeForm

@login_required
def change_password(request):
	if request.method=='POST':
		form=MyPasswordChangeForm(request.user,request.POST)
		print(request.POST)
		if form.is_valid():
			user=form.save()
			update_session_auth_hash(request,user)
			return redirect('myaccount')

	else:
		form = MyPasswordChangeForm(request.user)
		return render(request, 'account/change_password.html', {
'form': form
})




def Edit_account(request, account_id):
    myaccount = CustomUser.objects.get(pk=account_id)
    if request.method == "POST":
        form = Edit_userForm(request.POST, instance=myaccount)
        if form.is_valid():
            form.save()
            return redirect('myaccount')
    else:
        form = Edit_userForm(instance=myaccount)
    return render(request, 'account/edit_account.html', {'form': form})


#modified register user so that it redirects to login page after successfull registration
def register_user(request):
	if request.method == "POST":
		form = RegisterUserForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("Registration Successful!"))
			return redirect('login_view')
		
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
    return render(request,"account/realaccount.html", {'obj':obj})										
