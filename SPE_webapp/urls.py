from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_view,name='login_view'),
    path('home',views.home,name='home'),
    path('register_user',views.register_user,name='register_user'),
    path('Jobs',views.Jobs,name='Jobs'),
    path('add_post',views.add_post,name='add_post'),
    path('view_comments/<post_id>',views.view_comments,name='view_comments' ),
    path('add_comments/<post_id>',views.add_comment,name='add_comment'),
]