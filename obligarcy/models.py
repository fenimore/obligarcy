from django.db import models
from django.contrib.auth.models import User
#from django.utils import timezone


def pkgen():
    from hashlib import sha1
    from random import random
    pk = sha1(str(random()).encode('utf-8')).hexdigest().lower()[:6]
    return pk

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    # The additional attributes we wish to include.
    website = models.URLField(null=True)
    picture = models.ImageField(upload_to='profile_images', null=True)
    location = models.CharField(max_length='20', null=True)
    bio = models.CharField(max_length='144', null=True)
    # Mlehm/bio
    # Location
    def str(self):
        return self.user.username


class Submission(models.Model):
    id = models.CharField(max_length=6, primary_key=True, default=pkgen, unique=True)
    body = models.CharField(max_length=200)
    pub_date = models.DateTimeField('submitted')
    user = models.ForeignKey(User)
    # Word Count
    # FILE

    def __str__(self):
        return self.body


class Contract(models.Model):
    id = models.CharField(max_length=6, primary_key=True, default=pkgen, unique=True)
    preamble = models.CharField(max_length=150, null=True)
    conditions = models.CharField(max_length=400, null=True)
    penalties = models.CharField(max_length=200, null=True)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    frequency = models.CharField(max_length=2, default='O')
    deadline_has_past = models.BooleanField(default=False)
    users = models.ManyToManyField(User)
    submissions = models.ManyToManyField(Submission)
    # signing_deadline = models.DateTimeField('signing_deadline')

    def __str__(self):              # __unicode__ or str
        return self.preamble


class Deadline(models.Model):
    deadline = models.DateTimeField('deadline') #DateTimeField makes the sub form not accept
    submission = models.ForeignKey(Submission, null=True) # This has got to be many and many
    contract = models.ForeignKey(Contract)

    def __str__(self):              # __unicode__ or str
        string_deadline = self.deadline.strftime("%A %-d %b %Y")
        return string_deadline
