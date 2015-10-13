# -*- coding: utf-8 -*-
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from .models import Submission, Contract, UserProfile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs=
        {'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs=
        {'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password']


class UserProfileForm(forms.ModelForm):
    picture = forms.FileInput(attrs=
        {'class': 'form-control'})

    class Meta:
        model = UserProfile
        fields = ['picture']


class SubForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs=
        {'class': 'form-control'}))

    class Meta:
        model = Submission
        fields = ['body']


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
    body = forms.CharField(max_length=2000,
        widget=forms.Textarea(attrs={'class': 'form-control'}))
    end_date = forms.DateField(widget=SelectDateWidget(
        attrs={'class': 'form-control', 'style': "width:20%"}))
    start_date = forms.DateField(widget=SelectDateWidget(
        attrs={'class': 'form-control', 'style': "width:50%"}))
    frequency = forms.CharField(max_length=20, widget=forms.Select(
        attrs={'class': 'form-control'}, choices=FREQ))
    #http://getbootstrap.com/css/#forms-control-readonly
    #<input class="form-control" type="text" placeholder="Readonly input here…" readonly>
    first_signee = forms.ModelChoiceField(queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control',
            'style': "width:50%"}))
    second_signee = forms.ModelChoiceField(queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control',
             'style': "width:50%"}))
    third_signee = forms.ModelChoiceField(queryset=User.objects.all(),
         required=False, widget=forms.Select(attrs={'class':
              'form-control', 'style': "width:50%"}))
    fourth_signee = forms.ModelChoiceField(queryset=User.objects.all(),
         required=False, widget=forms.Select(attrs={'class':
              'form-control', 'style': "width:50%"}))

    class Meta:
        model = Contract
        fields = ['body', 'end_date', 'start_date', 'frequency']
