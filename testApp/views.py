from django.shortcuts import render,redirect
from testApp.models import *
from testApp import forms

# Create your views here.
def retrieve_view(request):
    employees=Employee.objects.all()
    return render(request,'testApp/retrieve.html',{'employees':employees})

def create_view(request):
    form=forms.EmployeeForm()
    if request.method=="POST":
        form=forms.EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'testApp/create.html',{'form':form})

def delete_view(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect("/")

def update_view(request,id):
    employee=Employee.objects.get(id=id)
    form=forms.EmployeeForm(instance=employee)
    if request.method=="POST":
        form=forms.EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect("/")
    return render(request,"testApp/update.html",{'form':form,'employee':employee})
