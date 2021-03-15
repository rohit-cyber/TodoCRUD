import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','crudfbvproject.settings')
import django
django.setup()

from testApp.models import *
from random import *
from faker import Faker

def populate(n):
    for i in range(n):
        faker=Faker()
        feno=randint(1001,9999)
        fename=faker.name()
        fesal=randint(10000,20000)
        fadrr=faker.city()
        emp_record=Employee.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eadrr=fadrr)
populate(25)
