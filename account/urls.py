from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_view,name='login_view'),
    path('register_user',views.register_user,name='register_user'),
    path('myaccount', views.myaccount,name='myaccount')

]