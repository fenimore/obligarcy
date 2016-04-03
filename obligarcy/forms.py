# -*- coding: utf-8 -*-
from functools import partial
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from .models import Submission, Contract, UserProfile, Deadline
from django.contrib.auth.models import User

# http://stackoverflow.com/questions/20700185/how-to-use-datepicker-in-django
# for the datepicker:
DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs=
        {'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs=
        {'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs=
            {'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class UserProfileForm(forms.ModelForm):
    picture = forms.FileInput()#attrs={'class': 'form-control'}
    location = forms.CharField(widget=forms.TextInput(attrs=
        {'class': 'form-control'}))
    bio = forms.CharField(widget=forms.TextInput(attrs=
            {'class': 'form-control'}))
    class Meta:
        model = UserProfile
        fields = ['picture', 'location', 'bio']


class SubForm(forms.Form):
    # here we use a dummy `queryset`, because ModelChoiceField
    # requires some queryset
    body = forms.CharField(widget=forms.Textarea(attrs=
        {'class': 'form-control','rows':'18'}))
    deadline = forms.ChoiceField(choices='[(m,m)]')

    def __init__(self, contract_id, user_id):
        super(SubForm, self).__init__()
        print((contract_id))
        print((user_id))
        # deadlines shown only for user
        dls = Deadline.objects.filter(contract=contract_id, signee=user_id, accomplished=False)
        print((dls.first()))
        submitter = User.objects.get(id=user_id)
        print((submitter))
        deadlines = []
        for deadline in dls:
            if submitter.submission_set.all():
                for sub in submitter.submission_set.all():
                    if deadline in sub.deadline_set.all():
                        print('user submitted already')
                        break
                    else:
                        if deadline not in deadlines:
                            deadlines.append(deadline)
                            print('user has nothing submitted')
                        else:
                            print(('deadline already added'))
            else:
                deadlines = dls
        deadline_tups = []
        for deadline in deadlines:
            tup = (deadline.id, deadline.deadline.date()) # On the date is relevant,
            deadline_tups.append(tup)                     # but its still good to keep things
        self.fields['deadline'].choices = deadline_tups  # in DateTime, stay consistent.
        #can believe that worked

class ContractForm(forms.ModelForm):
# https://docs.djangoproject.com/en/dev/topics/forms/#looping-over-the-form-s-fields
    FREQ = (
        ('O', 'Once off'),
        ('D', 'Daily'),
        ('2D', 'Every other day'),
        ('W', 'Weekly'),
        ('M', 'Monthly'),
        ('Y', 'Yearly'),
    )

    preamble = forms.CharField(max_length=150,
        widget=forms.Textarea(attrs={'class': 'form-control',
'placeholder': 'We the undersigned agree to this contract ...',
         'rows': '3'}))
    conditions = forms.CharField(max_length=400,
        widget=forms.Textarea(attrs={'class': 'form-control',
'placeholder': 'I must submit a movie review no less than 200 words every ...',
         'rows': '7'}))
    penalties = forms.CharField(max_length=200,
        widget=forms.Textarea(attrs={'class': 'form-control',
'placeholder': 'I agree to the aforementioned conditions on pain of ...',
         'rows': '5'}))
    end_date = forms.DateField(widget=DateInput())
    start_date = forms.DateField(widget=DateInput())
    frequency = forms.CharField(max_length=20, widget=forms.Select(
        attrs={'class': 'form-control'}, choices=FREQ))
    #http://getbootstrap.com/css/#forms-control-readonly
    #<input class="form-control" type="text" placeholder="…" readonly>

    class Meta:
        model = Contract
        fields = ['preamble','conditions','penalties', 'end_date', 'start_date', 'frequency']



"""
    deadline = forms.ModelChoiceField(queryset=Deadline.objects.none())

    def __init__(self, contract_id):
        super(SubForm, self).__init__()
        self.fields['deadline'].queryset = Deadline.objects.filter(contract=contract_id) # Somehow this works
"""
