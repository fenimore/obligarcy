from django.db import models
from django.contrib.auth.models import User
#from django.utils import timezone


class Submission(models.Model):
    body = models.CharField(max_length=200)
    pub_date = models.DateTimeField('submitted')
    user = models.ForeignKey(User)

    def __str__(self):
        return self.body


class Contract(models.Model):
    body = models.CharField(max_length=200)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    users = models.ManyToManyField(User)
    submissions = models.ManyToManyField(Submission)
    #deadline_has_past = models.BooleanField(False)

    def __str__(self):              # __unicode__ or str
        return self.body


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def str(self):
        return self.user.username