from django.http import HttpResponse
from django.shortcuts import render
from .models import User


# Create your views here.
def index(request):
    return HttpResponse('Hello World, here is users index')


def users(request):
    users_list = User.objects.all()
    return render(request, 'all_users.html', {'users': users_list})
