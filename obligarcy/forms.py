# -*- coding: utf-8 -*-
from django import forms
from .models import Submission, Contract, UserProfile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['picture', ]


class SubForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['body', ]


class ContractForm(forms.ModelForm):
    body = forms.CharField(max_length=128,
        widget=forms.Textarea(attrs={'class': 'form-control'}))
    #end_date = forms.DateField()
    first_signee = forms.ModelChoiceField(queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}))
    second_signee = forms.ModelChoiceField(queryset=User.objects.all())
    third_signee = forms.ModelChoiceField(queryset=User.objects.all(),
         required=False)
    fourth_signee = forms.ModelChoiceField(queryset=User.objects.all(),
         required=False)

    class Meta:
        model = Contract
        fields = ['body', 'end_date', 'start_date']


class ContractSigneeForm(forms.Form):
    first_signee = forms.ModelChoiceField(queryset=User.objects.all())
    second_signee = forms.ModelChoiceField(queryset=User.objects.all())
    third_signee = forms.ModelChoiceField(queryset=User.objects.all())
    fourth_signee = forms.ModelChoiceField(queryset=User.objects.all())
    #First two are mandatory
    #add to list, pass list
    #for every user in list,
    #u[1-3].contract_set.add(c)