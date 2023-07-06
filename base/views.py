from django.shortcuts import render

from .models import Departments,Doctor

from . forms import BookingForm
# Create your views here.
def home(request):
    return render(request, 'base/index.html')

def book(request):
    if request.method =="POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'base/confirmation.html')
            
    form = BookingForm() 
    dict_form={
        'form':form
    }
    return render(request, 'base/book.html',dict_form)

def dep(request):
    dict_dept={
        'dept': Departments.objects.all()
    }
    return render(request, 'base/dep.html',dict_dept)

def doctor(request):
    doct = Doctor.objects.all()
    return render(request, 'base/doc.html',{'doct' : doct})

