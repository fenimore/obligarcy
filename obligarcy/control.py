from .models import Submission, Contract, Deadline, UserProfile
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
# Functions
##########################

def activeContract(contract):
    if contract.start_date < timezone.now() < contract.end_date:
        contract.is_active = True
        contract.save()
    else:
        contract.is_active = False
        contract.save()

def activeContracts(contracts):
    for contract in contracts:
        activeContract(contract)
