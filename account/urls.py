from django.urls import path
from . import views
from django.contrib.auth.views import LoginView



urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('register_user/', views.register_user, name='register_user'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('Edit-account/<account_id>/', views.Edit_account,name='Edit_account'),
    path('change_password/', views.change_password, name='change_password'),

]