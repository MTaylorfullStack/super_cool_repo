from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *


def success(request):
    if 'user' not in request.session:
        return redirect('/')
    else:
        context = {
            'all_messages': Message.objects.all()
        }
        return render(request, "wall/success.html", context)

def add_message(request):
    poster = User.objects.get(id=request.session['id'])
    errors = Message.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/wall')
    else:
        new_message = Message.objects.create(message=request.POST['message'], poster=poster)
        return redirect('/wall')

def add_comment(request, message_id):
    new_comment = Comment.objects.create(comment=request.POST['comment'], poster=User.objects.get(id=request.session['id']), message=Message.objects.get(id=message_id))
    return redirect('/wall')

def editpage(request, message_id):
    one_message = Message.objects.get(id=message_id)
    message = {
        'one_message': one_message
    }
    #see user in sessions id
    if request.session['id'] == one_message.poster.id:
    #if user in sessions id is same as message posters id, they can see edit page
        return render(request, 'wall/edit.html', message)
    else:
        return redirect('/wall')
    #else, they get redirected to the wall
def save_edit(request, message_id):
    the_message = Message.objects.get(id=message_id)
    the_message.message = request.POST['message']
    the_message.save()
    return redirect('/wall')

def like(request, message_id):
    one_message = Message.objects.get(id=message_id)
    one_user = User.objects.get(id=request.session['id'])
    one_message.likes.add(one_user)
    return redirect('/wall')

def view_mess(request, message_id):
    context = {
        'one_message' : Message.objects.get(id=message_id)
    }
    return render(request, 'wall/one.html', context)


def destroy(request, message_id):
    one_message = Message.objects.get(id=message_id)
    one_message.delete()
    return redirect('/wall')

# Create your views here.
