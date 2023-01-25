from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from SPE_webapp.forms import  PostForm
from django.contrib import messages
from SPE_webapp.models import Jobs,Post,comments


def add_comment(request,post_id):
    if request.method == 'POST':
        text = request.POST['text']
        user = request.user
        post = Post.objects.get(id=post_id)
        comments.objects.create(text=text, user=user, post=post)
        return redirect('view_comments', post_id=post_id)
    else:
        return render(request, 'SPE_webapp/comments/add_comments.html')
		
def view_comments(request, post_id):
	val=post_id
	comment = comments.objects.filter(post=post_id)
	return render(request, 'SPE_webapp/comments/view_comments.html', {'comment': comment,'post_id':post_id,'val':val})

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


