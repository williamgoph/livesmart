# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import UserForm, GoalForm
from django.conf import settings
from .models import Profile, Goal
import crypt, sys

from django.contrib.auth.models import User


from django.contrib.auth.decorators import login_required


#@login_required(login_url="login/")

def index(request):
    if request.user.is_authenticated():
        return redirect('entries'); 
    else:
        return redirect('login');

def user(request):


    if request.method == 'POST':

        f = UserForm(request.POST)
        email = f['email'].value() 

        tmp = User.objects.filter(email=email)
        if tmp.count() > 0 and int(user_id) == 0:
            return HttpResponse("Username already exist!")

        user = User.objects.create_user(
            username=email,
            email=email,
            password=f['password'].value(),
            first_name=f['firstname'].value(),
            last_name=f['surname'].value()
        )
        
        profile = Profile()
        profile.user_id = user.id
        profile.dob = f['dob'].value()
        profile.save();
        return HttpResponse("User successfully created! Pls. login <a>href='login.html'</a>");
        
    else:
        """
        f = UserForm({
            'id': user.id,
            'firstname': user.firstname,
            'surname': user.surname,
            'dob': user.dob,
            'email': user.email,
            'password': user.password
        })
        """
    return render(request, 'nyresolution/user.html', {'form': UserForm})


#@login_required(login_url="../login/")
def goal(request, goal_id):

    if not request.user.is_authenticated():
        return redirect('login');

    goal = Goal.objects.filter(id = goal_id)
    goal = goal[0] if (goal.count() > 0) else Goal()

    f = None
    if request.method == 'POST':
        f = GoalForm(request.POST)
        goal.entry = f['entry'].value()
        goal.user_id = request.user.id
        goal.save();
        return redirect('entries');

    #else:
        #f = GoalForm({'id': goal.id, 'entry': goal.entry })

    return render(request, 'nyresolution/goal.html', {'goal': goal})


@login_required(login_url="../login/")
def entries(request):
    entries = Goal.objects.filter(user=request.user.id)
    user = request.user
    return render(request, 'nyresolution/entries.html', {'entries': entries, 'user':user})


    #return HttpResponse(request.user.id);

@login_required(login_url='../login/')
def delgoal(request, goal_id):
    Goal.objects.filter(id = goal_id).delete()
    return redirect('entries')
