from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *


def wallView(request):
    context = {
        'wallMessages'  :   Messages.objects.all(),
        'wallComments'  :   Comments.objects.all()
    }
    return render(request,"theWall.html",context)

def postMessage(request):
    name = request.session['username']
    user = Users.objects.filter(first_name = name)
    messageP = request.GET['message']
    m1 = Messages(message=messageP, user_id = Users.objects.get(id = user[0].id))
    m1.save()
    return redirect("/wall")

def postComment(request, id):
    name = request.session['username']
    user = Users.objects.filter(first_name = name)
    comment = request.GET['commentM']
    C1 = Comments(comment = comment, user_id = Users.objects.get(id = user[0].id),message_id = Messages.objects.get(id = int(id)) )
    C1.save()
    return redirect("/wall")

def deletemessage(request,id):
    m=Messages.objects.get(id=int(id))
    m.delete()
    return redirect("/wall")
# Create your views here.
