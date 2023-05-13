from django.shortcuts import render
from django.contrib.auth.models import User
#

from django.shortcuts import render

def index(request):
    return render(request,'main/index.html',{"user": request.user})


def about(request):
    return render(request, 'main/info.html', {"user": request.user})