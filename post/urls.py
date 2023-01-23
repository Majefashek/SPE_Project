from django.urls import path,include
from . import views
 
    
urlpatterns = [
    path('home',views.home,name='home'),
   
    path('Jobs',views.Jobs,name='Jobs'),
    path('add_post',views.add_post,name='add_post'),
    path('view_comments/<int:post_id>',views.view_comments,name='view_comments' ),
    path('add_comments/<post_id>',views.add_comment,name='add_comments'),
    
    
]  
    
    
    