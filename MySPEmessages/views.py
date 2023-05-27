from django.shortcuts import render
from django.http import JsonResponse
from .models import CustomUser,PrivateMessage
from django_ajax import decorators
from django.views.decorators.csrf import csrf_exempt
import uuid
from django.core import serializers
from django.urls import reverse

@csrf_exempt
def mycontacts(request):
    current_user=request.user
    contacts=CustomUser.objects.all().exclude(id=current_user.id)
    contact_details = [{'id': user.id, 'name': user.username, 'email': user.email} for user in contacts]
    return JsonResponse(contact_details, safe=False)


@csrf_exempt
def contact_room(request, reciever_id):
    theuser = request.user
    sender_id =request.user.id
    print(sender_id)
    print(reciever_id)
    chat_room_id = f"chat_{min(sender_id, int(reciever_id))}_{max(sender_id, int(reciever_id))}"
    data = {"chat_room_id": chat_room_id}
    return JsonResponse(data)



@csrf_exempt
def search_users(request):
    if request.POST:
        name_filter = request.POST['searched']
        current_user = request.user  # Get the current user
        users = CustomUser.objects.filter(username__icontains=name_filter).exclude(id=current_user.id)
        user_dicts = [{'id': user.id, 'name': user.username, 'email': user.email} for user in users]
        return JsonResponse(user_dicts, safe=False)
    else:
        return render(request, 'messages/mychat.html')

def mymessages(request):
    user_id=request.user.id
    return  render(request,'messages/mychat.html',{'user_id':user_id})

@csrf_exempt
def view_conversation(request, user_id):
    # Get the user object for the given user ID
    user2 = CustomUser.objects.get(id=user_id)
    # Retrieve the conversation between the current user and user2
    conversation = PrivateMessage.objects.get_conversation(request.user, user2)
    print(conversation)

    conversation_list = serializers.serialize('json', conversation)

    # Render the template with the conversation
    
    return JsonResponse(conversation_list,safe=False)

   

