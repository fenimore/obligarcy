from .models import Submission, Contract, Deadline, UserProfile, Action
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

from .forms import UserForm, UserProfileForm
from .forms import ContractForm, SubForm
from django.utils import timezone
from datetime import datetime, timedelta
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

import pandas as pd
from datetime import datetime
import time
import json

##########################
# Activity Stream
##########################
def create_action(actor, verb, target=None):
    # Check if a similiar action has occured in the last minute
    now = timezone.now()
    #last_minute = now - datetime.timedelta(seconds=60)
    #similar_actions = Action.objects.filter(actor_id=actor.id, verb=verb, timestamp_gte=last_minute)
    # If target
    # If not similar_actions page 186
    action = Action(actor=actor, verb=verb, target=target)
    action.save()

def get_stream(actor):
    user = User.objects.filter(id=actor.id).first()
    user_stream = []
    followers = user.userprofile.followed_by.all()
    for a in Action.objects.all():
        if a.actor.userprofile in followers:
            user_stream.append(a)
    return user_stream

##########################
# Eligibility
##########################
def checkEligibility(u_id, c_id, now):
    contract = Contract.objects.get(id=c_id)
    user = User.objects.get(id=u_id)
    followed_by = user.userprofile.followed_by.all()
    # Sois it's not begun, or it's still the first day
    if contract in user.contract_set.all():
        return False
    if(now < contract.start_date) or ((now - contract.start_date) < timedelta(1)):
        for u in contract.users.all():
            if u.userprofile in followed_by:
                return True
        return False
    return False



##########################
# Functions
##########################

def activeContract(contract):
    # if contract is not completed

    if contract.start_date < timezone.now() < contract.end_date:
        contract.is_active = True
        contract.save()
    else:
        contract.is_active = False
        contract.save()

def activeContracts(contracts):
    for contract in contracts:
        activeContract(contract)

def expireDeadlines(deadlines):
    for dl in deadlines:
        if dl.deadline < timezone.now():
            if dl.is_expired == False:
                # Send Action User missed Deadline
                dl.is_expired = True
                dl.save()
        else:
            dl.is_expired = False
            dl.save()

def completeContract(contract, user):
    u = User.objects.get(id=user)
    for dl in u.deadline_set.filter(contract=contract):
            if not dl.is_accomplished or dl.is_late:
                return False
    c = Contract.objects.get(id=contract)
    c.completed_by.add(user)
    c.save()
    return True
