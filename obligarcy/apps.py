#dashboard.apps.py
from django.apps import AppConfig
from actstream import registry
from django.contrib.auth.models import User
from models import Contract, Deadline, Submission

class MyAppConfig(AppConfig):
    name = 'obligarcy'
    def ready(self):
        registry.register(User, self.get_model('Contract')) #self.get_model('Submission'),self.get_model('Deadline')
        registry.register(Contract)
