from django.shortcuts import render
from .models import UserFields
from .forms import UserFormFields
def list_users(request):
    users = UserFields.objects.all()
    return render(request,'list_users.html', {'users':users})

def create_users(request):
    form = UserFormFields()
    return render(request,'create_users.html',{'form':form})

def update_users():
    pass

def delete_users():
    pass
