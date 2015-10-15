from django.shortcuts import render, get_object_or_404
from .models import Submission, Contract, Deadline
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

from .forms import UserForm, UserProfileForm
from .forms import ContractForm, SubForm
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

import pandas as pd
from datetime import datetime
import json

#from pytagcloud import create_tag_image, make_tags
#from pytagcloud.lang.counter import get_tag_counts

def index(request):
    return render(request, 'obligarcy/index.html')


##########################
# User Views
##########################
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        #profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid():
            print(('yup'))
        if user_form.is_valid():# and profile_form.is_valid()
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            #profile = profile_form.save(commit=False)
            #profile.user = user
            #profile.email = request.POST['email']
            #profile.location = request.POST['location']
            #if 'picture' in request.FILES:
            #    profile.picture = request.FILES['picture']
            #profile.save()
            registered = True
            return HttpResponseRedirect('/login/')
        else:
            print((user_form.errors))#, profile_form.errors
    user_form = UserForm()
    profile_form = UserProfileForm()
    return render(request, 'obligarcy/register.html',
         {'user_form': user_form, 'profile_form': profile_form})


def user_login(request):
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                request.session['username'] = user.username
                request.session['id'] = user.id
                return HttpResponseRedirect('/profile/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Account no longer active.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print(("Invalid login details: {0}, {1}".format(username, password)))
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'obligarcy/login.html')


def user_logout(request):
    logout(request)
    request.session['username'] = None
    request.session['id'] = None
    return HttpResponseRedirect('/')


def profile(request):
    user_id = request.session['id']
    user = get_object_or_404(User, id=user_id)
    #print((user.userprofile.picture.path))
    posts = user.submission_set.all()
    contracts = user.contract_set.all()
    return render(request, 'obligarcy/profile.html',
        {'contracts': contracts, 'posts': posts})
     # {'user': user, 'posts': posts}


def show_prof(request, user_id):
    user = get_object_or_404(User, id=user_id)
    posts = user.submission_set.all()
    contracts = user.contract_set.all()
    return render(request, 'obligarcy/profile.html',
        {'contracts': contracts, 'posts': posts, 'user': user})


##########################
# Submission Views
##########################
def show_sub(request, submission_id):
    template = 'obligarcy/submission.html'
    submission = get_object_or_404(Submission, id=submission_id)
    author = submission.user
    contracts = submission.contract_set.all()
    word_count = len(submission.body.split())
    deadline = submission.deadline_set.all().first()
    for c in contracts:
        contract = c
    return render(request, template, {'submission': submission,
         'author':author, 'contract':contract, 'word_count':word_count,
          'deadline':deadline})


def submit(request, contract_id):
    if request.method == 'POST':
        form = SubForm(request.POST)
        #print((form['deadline']))
        #if form.is_valid():
        author = User.objects.get(id=request.session['id'])
        print((author))
        contract = Contract.objects.get(id=contract_id)
        print((contract))
        body = request.POST['body']
        print((body))
        new_sub = Submission(body=body, pub_date=timezone.now(), user=author)
        new_sub.save()
        new_sub.contract_set.add(contract)
        new_sub.save()
        c = new_sub.contract_set.all().first()
        deadline_id = request.POST['deadline']
        d = Deadline.objects.get(id=deadline_id)
        new_sub.deadline_set.add(d)
        new_sub.save()
        word_count = len(new_sub.body.split())
        return render(request, 'obligarcy/submission.html',
                    {'submission': new_sub, 'contract': c,
                         'word_count': word_count, 'deadline': d})
        #else:
        #    print(('form not valid?'))
        #    return render(request, 'obligarcy/submit.html', {'error_message':'something went wrong'})
    else:
        contract_id = contract_id
        form = SubForm(contract_id)
        #contract_id = contract_id
        c = Contract.objects.get(id=contract_id)
        dls = c.deadline_set.all()
        deadlines = []
        for deadline in dls:
            if not deadline.submission:
                deadlines.append(deadline) # This won't work until I can get the form to work
        return render(request, 'obligarcy/submit.html', {'form': form,
         'contract_id': contract_id, 'deadlines': deadlines})
         #'form': form,
#TODO: get form to work with deadlines so that I can prune the completed deadlines
#TODO: and so that I can store the data as DateField, so it displays better
#TODO: Change DateTimeField to DateField

##########################
# Contract Views
##########################
def show_con(request, contract_id):
    contract = get_object_or_404(Contract, id=contract_id)
    signees = contract.users.all()
    submissions = contract.submissions.all()
    deadlines = contract.deadline_set.all()
    return render(request, 'obligarcy/contract.html', {'contract': contract,
    'signees': signees, 'submissions': submissions,  'deadlines':deadlines})


def challenge(request):
    if request.method == 'POST':
        print('is post')
        contract_form = ContractForm(data=request.POST)
        if contract_form.is_valid():
            print('Valid Form')
            contract = contract_form.save()
            contract.save()
            u1 = User.objects.get(id=request.POST['first_signee'])
            u1.contract_set.add(contract)
            if request.POST['second_signee']:
                u2 = User.objects.get(id=request.POST['second_signee'])
                u2.contract_set.add(contract)
            if request.POST['third_signee']:
                u3 = User.objects.get(id=request.POST['third_signee'])
                u3.contract_set.add(contract)
            if request.POST['fourth_signee']:
                u4 = User.objects.get(id=request.POST['fourth_signee'])
                u4.contract_set.add(contract)
            if contract.frequency == 'O':
                deadline_list = []
                deadline = str(request.POST['end_date'])
                d = Deadline(deadline=deadline, contract_id=contract.id)
                d.save()
            else:
                deadline_list = pd.date_range(contract.start_date,
                 contract.end_date, freq=contract.frequency)
                deadline_list = deadline_list.to_pydatetime()
                for deadline in deadline_list:
                    deadline = str(deadline) # I have to string it, else it won't work with forms?
                    d = Deadline(deadline=deadline, contract_id=contract.id)
                    d.save()
            contract.save()
            signees = contract.users.all()
            deadlines = contract.deadline_set.all()
            return render(request, 'obligarcy/contract.html',
                {'contract': contract, 'signees': signees, 'deadlines':deadlines})
        else:
            print((contract_form.errors))
    contract_form = ContractForm()
    #contract_signee_form = ContractSigneeForm()
    return render(request, 'obligarcy/challenge.html',
            {'contract_form': contract_form})

##########################
# Combo Views
##########################

def firehose(request):
    contracts = Contract.objects.all()
    users = User.objects.all()
    submissions = Submission.objects.all()
    return render(request, 'obligarcy/firehose.html', {'contracts': contracts,
         'users':users ,'submissions':submissions})
