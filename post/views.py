from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect,get_object_or_404
from SPE_webapp.forms import  PostForm
from django.contrib import messages
from SPE_webapp.models import Jobs, Post, Comments
from .models import likes
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect

def dislike(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    user = request.user
    likes.objects.filter(post=post, user=user).delete()
    like_count = post.likes_set.count()
    return JsonResponse({'like_count':like_count})

@csrf_protect
def like_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    user = request.user
    if not likes.objects.filter(post=post, user=user).exists():
        likes.objects.create(post=post, user=user)
        like_count = post.likes_set.count()
        return JsonResponse({'like_count':like_count})


def add_comment(request,post_id):
    if request.method == 'POST':
        text = request.POST['text']
        user = request.user
        post = Post.objects.get(id=post_id)
        comments.objects.create(text=text, user=user, post=post)
        return redirect('view_comments', post_id=post_id)
    else:
        return render(request, 'post/comments/add_comments.html')

		
def view_comments(request, post_id):
	val=post_id
	comment = comments.objects.filter(post=post_id)
	return render(request, 'post/comments/view_comments.html', {
        'comment': comment,
        'post_id':post_id,
        'val':val,
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
    return render(request, 'post/add_post.html', {'form': form})



jobs = Jobs.objects.all()
 
def Jobs(request):
    if request.user.is_authenticated and request.user.is_admin:
        return render(request, 'SPE_webapp/Jobs.html', {'jobs': jobs})
    else:
        return render(request,'SPE_webapp/myjobs.html',{'jobs':jobs})


