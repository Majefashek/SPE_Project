from django.shortcuts import render
from django.http import JsonResponse
from .models import CustomUser
from django_ajax import decorators
from django.views.decorators.csrf import csrf_exempt
import uuid

@csrf_exempt
def contact_room(request,reciever_id):
    user=request.user
    sender_id=user.id
    reciever_id=sender_id
    context={'sender_id':sender_id ,'reciever_id':reciever_id }
    return JsonResponse(context, safe=False)

@csrf_exempt
def search_users(request):
    if request.POST:
        name_filter = request.POST['searched']
        users = CustomUser.objects.filter(username__icontains=name_filter)
        user_dicts = [{'id': user.id, 'name': user.username, 'email': user.email} for user in users]
        return JsonResponse(user_dicts, safe=False)
    else:
        return render(request, 'messages/messages.html')

def mymessages(request):
    return  render(request,'messages/messages.html')
# Create your views here.
