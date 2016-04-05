from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Submission, Contract, Deadline, UserProfile
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required

from .forms import UserForm, UserProfileForm
from .forms import ContractForm, SubForm
from .control import completeContract, activeContract, activeContracts, checkEligibility
from django.utils import timezone
from datetime import datetime, timedelta
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

import pandas as pd
from datetime import datetime
import time
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
        profile_form = UserProfileForm(data=request.POST)
        print((request.POST['bio']))
        #print((profile_form.location))
        #print((profile_form))
        if profile_form.is_valid():
            print(('yup'))
        if user_form.is_valid():# and profile_form.is_valid()
            user = user_form.save()
            pswd = user.password # for immediate log in
            user.set_password(user.password)
            user.save()
            # DO profile attributes, OneToOneField with User
            # Form somereason saving the form doesnt work. profile form won't validate
            profile = UserProfile(bio=request.POST['bio'], location=request.POST['location'], user=user)
            #profile = profile_form.save(commit=False)
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
            u = authenticate(username=user.username, password=pswd)
            login(request, u)
            request.session['username'] = user.username
            request.session['id'] = user.id
            return HttpResponseRedirect('/profile/')
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

# TODO: Add Prochaine Deadlines
@login_required(login_url='/login/')
def profile(request):
    user_id = request.session['id']
    user = get_object_or_404(User, id=user_id)
    #print((user.userprofile.picture.path))
    posts = user.submission_set.all()
    contracts = user.contract_set.all()
    deadlines = Deadline.objects.filter(signee=user,
        is_expired=False, is_accomplished=False).order_by('deadline')
    # Completed Contracts
    completed_contracts = []
    for c in contracts:
        if user in c.completed_by.all():
            completed_contracts.append(c)
    # Get Follows and followed_by
    follows = user.userprofile.follows.all()
    followed_by = user.userprofile.followed_by.all() # followed_by.user
    return render(request, 'obligarcy/profile.html',
        {'contracts': reversed(contracts), 'profile': user, 'posts': reversed(posts),
        'deadlines':deadlines, 'completed':completed_contracts,
        'follows':follows, 'followed_by':followed_by})
    return render(request, 'obligarcy/profile.html',
        {'contracts': contracts, 'posts': reversed(posts[:4]), 'profile': user,
        'completed':completed_contracts, 'deadlines':deadlines,
        'follows':follows[:4], 'followed_by':followed_by[:4],
        'can_follow':can_follow, 'already_follows': already_follows})
@login_required(login_url='/login/')
def show_prof(request, user_id):
    browser = User.objects.get(id=request.session['id'])
    user = get_object_or_404(User, id=user_id)
    posts = user.submission_set.all()
    contracts = user.contract_set.all()
    deadlines = Deadline.objects.filter(signee=user,
        is_expired=False, is_accomplished=False).order_by('deadline')
    # Completed Contracts
    completed_contracts = []
    for c in contracts:
        if user in c.completed_by.all():
            completed_contracts.append(c)
    # Get Follows and followed_by
    follows = user.userprofile.follows.all()
    followed_by = user.userprofile.followed_by.all() # followed_by.user
    # Following
    can_follow = False
    already_follows = False
    if int(user_id) != int(request.session['id']):
        can_follow = True
    if browser.userprofile in followed_by:
        already_follows = True
    return render(request, 'obligarcy/profile.html',
        {'contracts': contracts[:4], 'posts': posts[:4], 'profile': user,
        'completed':completed_contracts[:4], 'deadlines':deadlines,
        'follows':follows[:4], 'followed_by':followed_by[:4],
        'can_follow':can_follow, 'already_follows': already_follows})

@login_required(login_url='/login/')
def follow(request, user_1_id, user_2_id): # 1 is Who, 2 is Whom
    u1 = User.objects.get(id=user_1_id)
    u2 = User.objects.get(id=user_2_id)
    u1.userprofile.follows.add(u2.userprofile)
    u1.save()
    print(user_1_id, user_2_id, u2.userprofile)
    print(u1.userprofile.follows.get(id=u2.id).user.username)
    return HttpResponseRedirect('/user/' + user_2_id) # After POST redirect

@login_required(login_url='/login/')
def unfollow(request, user_1_id, user_2_id): # 1 is Who, 2 is Whom
    u1 = User.objects.get(id=user_1_id)
    u2 = User.objects.get(id=user_2_id)
    u1.userprofile.follows.remove(u2.userprofile)
    u1.save()
    return HttpResponseRedirect('/user/' + user_2_id) # After POST redirect


##########################
# Submission Views
##########################
@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def submit(request, contract_id, user_id):
    if request.method == 'POST':
        form = SubForm(request.POST, user_id)
        #if form.is_valid():
        author = User.objects.get(id=request.session['id'])
        contract = Contract.objects.get(id=contract_id)
        body = request.POST['body']
        dl = Deadline.objects.get(id=request.POST['deadline'])
        new_sub = Submission(body=body, pub_date=timezone.now(), user=author)
        new_sub.save()
        dl.submission = new_sub
        if dl.deadline < timezone.now():
            dl.is_expired = True
            dl.save()
            dl.is_late = True
        dl.is_accomplished = True
        dl.save()
        new_sub.contract_set.add(contract)
        new_sub.save()
        c = new_sub.contract_set.all().first()
        new_sub.save()
        completeContract(contract_id, user_id)
        return HttpResponseRedirect('/submission/' + new_sub.id) # After POST redirect
    else:
        contract_id = contract_id
        print(request.session['id'])
        author = User.objects.get(id=request.session['id'])
        form = SubForm(contract_id, request.session['id'])
        #contract_id = contract_id
        c = Contract.objects.get(id=contract_id)
        return render(request, 'obligarcy/submit.html', {'form': form,
         'contract_id': contract_id, 'user_id':request.session['id']})


##########################
# Contract Views
##########################
@login_required(login_url='/login/')
def show_con(request, contract_id):
    contract = get_object_or_404(Contract, id=contract_id)
    activeContract(contract)
    allow_signing = checkEligibility(request.session['id'], contract_id, timezone.now())
    signees = contract.users.all()
    for dl in contract.deadline_set.all():
        if dl.deadline < timezone.now():
            dl.is_expired = True
            dl.save()
        else:
            dl.is_expired = False
            dl.save()
    dls = signees[0].deadline_set.filter(contract=contract)
    return render(request, 'obligarcy/contract.html', {'contract': contract, 'allow_signing':allow_signing, 'signees': signees, 'deadlines': dls})

@login_required(login_url='/login/')
def challenge(request):
    if request.method == 'POST':
        print('is post')
        contract_form = ContractForm(data=request.POST)
        if contract_form.is_valid():
            print('Valid Form')
            contract = contract_form.save()
            contract.save()
            u = User.objects.get(id=request.session['id']) # Set the
            u.contract_set.add(contract)   # default to sessions.users
            # This can be taken out, now? Or maybe commented out?)
            """
            if request.POST['second_signee']:# and maybe make it unchangeable?
                u2 = User.objects.get(id=request.POST['second_signee']) # These forms will be deleted
                u2.contract_set.add(contract)
            if request.POST['third_signee']:
                u3 = User.objects.get(id=request.POST['third_signee'])
                u3.contract_set.add(contract)
            if request.POST['fourth_signee']:
                u4 = User.objects.get(id=request.POST['fourth_signee'])
                u4.contract_set.add(contract)
            """
            if contract.frequency == 'O': # Once off
                deadline_list = []
                deadline = contract.end_date # Duh
                deadline = deadline.replace(hour=23, minute=59)
                is_expired = timezone.now() > deadline
                d = Deadline(deadline=deadline, contract_id=contract.id,
                             signee=u, is_expired=is_expired)
                d.save()
            else:
                deadline_list = pd.date_range(contract.start_date,
                 contract.end_date, freq=contract.frequency)
                deadline_list = deadline_list.to_pydatetime()
                for deadline in deadline_list:
                    deadline = deadline # first argument hour, second minute # Should I str this? If i must..
                    deadline = deadline.replace(hour=23, minute=59)
                    is_expired = timezone.now() > deadline
                    d = Deadline(deadline=deadline, contract_id=contract.id,
                                 signee=u, is_expired=is_expired)
                    d.save()
            #contract.start_date = contract.start_date.replace(hour=23, minute=59)
            contract.end_date = contract.end_date.replace(hour=23, minute=59)
            contract.save()
            signees = contract.users.all() # what am I do?
            deadlines = contract.deadline_set.all() # What happens here?
            return HttpResponseRedirect('/contract/'+contract.id)
        else:
            print((contract_form.errors))
    contract_form = ContractForm()
    return render(request, 'obligarcy/challenge.html',
            {'contract_form': contract_form})

@login_required(login_url='/login/')
def sign_con(request, contract_id): # As of now, it will appear (the sign button)
    # Crucial! Nice save!
    if not checkEligibility(request.session['id'], contract_id, timezone.now()):
        return HttpResponseRedirect('/contract/'+contract_id)

    if request.method == 'POST':   # only if it has been less than a day after the
        contract = Contract.objects.get(id=contract_id) # contract start date
        user = User.objects.get(username=request.POST['signee'])
        contract.users.add(user)
        contract.save()
        deadlines = contract.deadline_set.all()
        for deadline in deadlines:
            d = Deadline(deadline=deadline.deadline, contract_id=contract.id,
                                 signee=user)
            d.save()
        return HttpResponseRedirect('/contract/'+contract.id)
    else:
        contract = Contract.objects.get(id=contract_id)
        return render(request, 'obligarcy/sign.html', {'contract': contract})

@login_required(login_url='/login/')
def show_active(request, user_id):
    contracts = get_list_or_404(Contract.objects.order_by('-start_date'), users=user_id)
    map(activeContract, contracts)
    active_contracts = []
    for con in contracts:
        if con.is_active:
            active_contracts.append(con)
    return render(request, 'obligarcy/active.html', {'contracts': active_contracts})

##########################
# Combo Views
##########################

def firehose(request):
    contracts = Contract.objects.all()
    users = User.objects.all()
    submissions = Submission.objects.all()
    return render(request, 'obligarcy/firehose.html', {'contracts': reversed(contracts),
         'users':reversed(users) ,'submissions':reversed(submissions)})
