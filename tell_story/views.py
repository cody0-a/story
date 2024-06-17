from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import *
from .models import *


app_name = "tell_story"


def index(request):
    return render(request, 'tell_story/base.html')


def rooms(request):
    return  render(request, 'tell_stroy/rooms.html')


def room_details(request,room_id):
    return render(request, 'tell_story/room_detail.html')


def stories(request):
    return render(request, 'tell_story/stories.html')


def self_story(request):
    return render(request, 'tell_story/self_story.html')


def add_story(request):
    return render(request,'tell_story/add_story.html')


def edit_story(request,story_id):
    return render(request,'tell_story/edit_story.html')

def delete_story(request,story_id):
    return render(request,'tell_story/delete_story.html')


def add_comment(request,story_id):
    return render(request,'tell_story/add_comment.html')

