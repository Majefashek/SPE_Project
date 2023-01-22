from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import RegisterUserForm, PostForm
from django.contrib import messages
from .models import Post, Jobs, Comments
from django.contrib.auth import get_user_model


def add_comment(request, post_id):
    if request.method == 'POST':
        text = request.POST['text']
        user = request.user
        post = Post.objects.get(id=post_id)
        Comments.objects.create(text=text, user=user, post=post)
        return redirect('view_comments', post_id=post_id)
    else:
        return render(request, 'comments/add_comments.html')
		
def view_comments(request, post_id):
	post_id = int(post_id)
	comment = Comments.objects.filter(post=post_id)
	return render(request, 'SPE_webapp/comments/view_comments.html', {
		'comment': comment,'post_id':post_id
		})


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'SPE_webapp/add_post.html', {'form': form})

   
jobs = Jobs.objects.all()
 
def Jobs(request):
    if request.user.is_authenticated and request.user.is_admin:
        return render(request, 'SPE_webapp/Jobs.html', {'jobs': jobs})
    else:
        return render(request,'SPE_webapp/myjobs.html',{'jobs':jobs})


def home(request):
	if request.method == 'POST':
		post = Post.objects.all()
		return render(request,'SPE_webapp/home.html', {'post':post})
	else:
		messages.success(request, ('You are required to login in order to accesss this site'))
		return redirect('login_view')
	
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
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		print(username)
		print(password)
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			print(request.user)
			return redirect('home')

		else:
			print('user not authenticated')
			messages.error(request, ("There Was An Error Logging In, Try Again..."))	
			return redirect('login_view')
	else:
		return render(request, "SPE_webapp/index.html", {})


	









