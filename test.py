from obligarcy.models import *
from actstream import action 

u = User.objects.all()[0]
c = u.contract_set.all()[0]

def testaction1(u):
    action.send(u, verb="is")

def testaction2(u, c):
    action.send(u, verb="signed", target=c)
