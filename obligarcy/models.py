from django.db import models
from django.contrib.auth.models import User
#from django.utils import timezone


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def str(self):
        return self.user.username


class Submission(models.Model):
    body = models.CharField(max_length=200)
    pub_date = models.DateTimeField('submitted')
    user = models.ForeignKey(User)
    # Word Count

    def __str__(self):
        return self.body


class Contract(models.Model):
    body = models.CharField(max_length=200)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    frequency = models.CharField(max_length=2, default='O')
    deadline_list = models.CharField(max_length=3000, default='')
    deadline_has_past = models.BooleanField(default=False)
    users = models.ManyToManyField(User)
    submissions = models.ManyToManyField(Submission)
    #deadline_has_past = models.BooleanField(False)

    def __str__(self):              # __unicode__ or str
        return self.body


class Deadline(models.Model):
    deadline = models.DateTimeField('deadline')
    submission = models.ForeignKey(Submission)
    contract = models.ForeignKey(Contract)

    def __str__(self):              # __unicode__ or str
        return self.deadline

