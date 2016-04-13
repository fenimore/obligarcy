from obligarcy.models import *
from obligarcy.control import *

u = User.objects.all()[0]
c = u.contract_set.all()[0]


