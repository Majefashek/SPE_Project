from django.urls import path,include
from . import views

urlpatterns = [
    path('',include('account.urls')),
    path('post',include('post.urls')),
    
]