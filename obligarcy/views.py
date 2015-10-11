from django.shortcuts import render, get_object_or_404
from .models import Submission, Contract
from django.contrib.auth.models import User
from .forms import UserForm, UserProfileForm
from .forms import SubForm, ContractForm, ContractSigneeForm
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'obligarcy/index.html')

#def show_prof(request, user_id):
#    user = get_object_or_404(User, id=user_id)
#    posts = user.submission_set.all()
    #contracts = user.contract_set.all()
#    return render(request, 'obligarcy/profile.html', {'user': user, 'posts': posts})


# ALL profiles


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
            return HttpResponseRedirect('/obligarcy/login/')
        else:
            print((user_form.errors, profile_form.errors))
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
                return HttpResponseRedirect('/obligarcy/')
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
    return HttpResponseRedirect('/obligarcy')


def profile(request):
    #user_id GET FROM SESSION
    #user = get_object_or_404(User, id=user_id)
    #posts = user.submission_set.all()
    #contracts = user.contract_set.all()
    return render(request, 'obligarcy/profile.html')
     # {'user': user, 'posts': posts}


def show_sub(request, submission_id):
    template = 'obligarcy/submission.html'
    submission = get_object_or_404(Submission, id=submission_id)
    return render(request, template, {'submission': submission})


def submit(request):
    if request.method == 'POST':
        form = SubForm(request.POST)
        if form.is_valid():
            author = User.objects.get(id=request.POST['user'])
            new_sub = Submission(body=form.cleaned_data['body'],
                pub_date=timezone.now(), user=author)  # required
            new_sub.save()
            return render(request, 'obligarcy/submission.html',
                {'submission': new_sub})
    else:
        form = SubForm()
    return render(request, 'obligarcy/submit.html', {'form': form})


# ALL submissions by profile
# ALL submissions by contract


def show_con(request, contract_id):
    contract = get_object_or_404(Contract, id=contract_id)
    return render(request, 'obligarcy/contract.html', {'contract': contract})


def challenge(request):
    if request.method == 'POST':
        contract_form = ContractForm(request.POST)
        contract_signee_form = ContractSigneeForm(request.POST)
        if contract_form.is_valid() and contract_signee_form:
            contract = contract_form.save()
            return render(request, 'obligarcy/contract.html',
                {'contract': contract})
    else:
        contract_form = ContractForm()
        contract_signee_form = ContractSigneeForm()
    return render(request, 'obligarcy/submit.html',
             {'contract_form': contract_form})
            # {'contract_signee_form': contract_signee_form}
# ALL contracts
# ALL contracts by profile

# Create User
# Create Submission
# Create Contract

