# coding:utf-8
from django.shortcuts import render

# Create your views here.
from .models import UserMessage

def getform(request):
    # 从数据库中取值
    # all_messages = UserMessage.objects.all()
    # for message in all_messages:
    #     print message.name

    # 从数据库删除值
    # all_messages = UserMessage.objects.filter(name='Tom')
    # all_messages.delete()
    # for message in all_messages:
    #     message.delete()

    # 向数据库中写入值
    # if request.method == 'POST':
    #     name = request.POST.get('name', '')
    #     message = request.POST.get('message', '')
    #     address = request.POST.get('address', '')
    #     email = request.POST.get('email', '')
    #     user_message = UserMessage()
    #     user_message.name = name
    #     user_message.message = message
    #     user_message.address = address
    #     user_message.email = email
    #     user_message.object_id = 'Tom_id'
    #     user_message.save()

    return render(request, 'message_form.html')