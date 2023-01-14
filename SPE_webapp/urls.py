from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_view,name='login_view'),
    path('home',views.home,name='home'),
    path('register_user',views.register_user,name='register_user'),
    path('Jobs',views.Jobs,name='Jobs'),
    path('add_image',views.add_image,name='add_image')
]