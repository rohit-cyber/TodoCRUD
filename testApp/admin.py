from django.contrib import admin
from testApp.models import *

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','esal','eadrr']

admin.site.register(Employee,EmployeeAdmin)
