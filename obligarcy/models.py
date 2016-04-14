from django.db import models
from django.contrib.auth.models import User
from easy_thumbnails.fields import ThumbnailerImageField
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

#from django.utils import timezone


def pkgen():
    from hashlib import sha1
    from random import random
    pk = sha1(str(random()).encode('utf-8')).hexdigest().lower()[:6]
    return pk


# Activity Streams
# TODO: Add Action on deadline expire
# TODO: Fix Create Action Method
class Action(models.Model):
    actor = models.ForeignKey(User, related_name='actions', db_index=True)
    verb = models.CharField(max_length=255)
    target_ct = models.ForeignKey(ContentType, blank=True, null=True,
                                    related_name='target_obj')
    target_id = models.SlugField(null=True, blank=True,
                                                db_index=True)
    target = GenericForeignKey('target_ct', 'target_id')
    pub_date = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):              # __unicode__ or str
        string_action = self.actor.username + " " + self.verb
        if self.target:
            string_action += " " + str(self.target)[:15]
        return string_action


# The default user constructor is:
#
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, null=True) #   OneToOneField(User)
    # The additional attributes we wish to include.
    website = models.URLField(null=True)
    picture = ThumbnailerImageField(upload_to='profile_images', null=True)
    location = models.CharField(max_length=20, null=True)
    bio = models.CharField(max_length=144, null=True)
    follows = models.ManyToManyField('UserProfile', related_name='followed_by')

    def str(self):
        return self.user.username


class Submission(models.Model):
    id = models.CharField(max_length=6, primary_key=True, default=pkgen, unique=True)
    body = models.CharField(max_length=200, null=True)
    media = ThumbnailerImageField(upload_to='submissions/%Y/%m/%d', null=True)
    pub_date = models.DateTimeField('submitted')
    user = models.ForeignKey(User)
    is_media = models.BooleanField(default=False)
    # This Generic Relation allows backward Queries from Contract/Dl etc.
    activities = GenericRelation(Action, related_query_name='activities',
                                    object_id_field="target_id",
                                    content_type_field='target_ct')
    # Word Count
    # FILE

    def __str__(self):
        if not self.is_media:
            return self.body
        elif self.is_media:
            return "This is "+ user.username +"\'s Media Submission"

# Add active
class Contract(models.Model):
    id = models.CharField(max_length=6, primary_key=True, default=pkgen, unique=True)
    title = models.CharField(max_length=60, null=True)
    conditions = models.CharField(max_length=400, null=True)
    small_print = models.CharField(max_length=200, null=True)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    frequency = models.CharField(max_length=2, default='O')
    is_active = models.BooleanField(default=False)
    users = models.ManyToManyField(User) # signee
    submissions = models.ManyToManyField(Submission)
    completed_by = models.ManyToManyField(User, related_name='has_completed')
    # This Generic Relation allows backward Queries from Contract/Dl etc.
    activities = GenericRelation(Action, related_query_name='activities',
                                    object_id_field="target_id",
                                    content_type_field='target_ct')

    def __str__(self):              # __unicode__ or str
        return self.title

# add a signee for the
class Deadline(models.Model):
    deadline = models.DateTimeField('deadline') #DateTimeField makes the sub form not accept
    submission = models.ForeignKey(Submission, null=True) # This has got to be many and many
    contract = models.ForeignKey(Contract)
    signee = models.ForeignKey(User)
    is_accomplished = models.BooleanField(default=False)
    is_late = models.BooleanField(default=False)
    is_expired = models.BooleanField(default=False)
    # This Generic Relation allows backward Queries from Contract/Dl etc.
    activities = GenericRelation(Action, related_query_name='activities',
                                    object_id_field="target_id",
                                    content_type_field='target_ct')


    def __str__(self):              # __unicode__ or str
        string_deadline = self.deadline.strftime("%A %-d %b %Y")
        return string_deadline
