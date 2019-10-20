from django.http import HttpResponse, JsonResponse,FileResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.forms.models import model_to_dict
from django.core import serializers
from main.forms import *
from main.models import *
from main.decorators import *
import json
from django.conf import settings
from django.template.loader import render_to_string
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordResetForm
import requests

def index(request):
    return render(request,"layouts/index.html")

def events_login(request):
    if request.user.is_authenticated:
        if request.user.is_student:
            return redirect("/student")
    if request.method=="POST":
        username = User.objects.filter(email=request.POST['email']).first()
        if username is None:
            return render(request, 'layouts/login.html',{"messages":[["text-danger","Email Not Found."]]})            
        username = username.username
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user, backend='django.contrib.auth.backends.AllowAllUsersModelBackend')
            if request.user.is_student:
                return redirect("/student")
        else:
            return render(request, 'layouts/login.html',{"messages":[["text-danger","Invalid Credentials."]]})
    return render(request, 'layouts/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def redirect_ac(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        if request.user.is_student:
            return redirect("/student")

def get_courses(request):
    if request.method=="POST":
        dept_id = request.POST.get('department')
        dept = Department.objects.filter(id=int(dept_id)).first()
        courses = Course.objects.filter(department=dept).order_by('name')
        data = [course.as_dict() for course in courses]
        return JsonResponse(data,safe=False)

def misc_upload(request):
    msg = ""
    if request.method == 'POST':
        form = MiscUpload(request.POST, request.FILES)
        if form.is_valid():
            analysis = form.save(commit=False)
            analysis.user = request.user
            if request.user.is_student:
                analysis.is_approved = 0
            else:
                analysis.is_approved = 1
            analysis.save()
            msg = "Uploaded successfully"
            return render(request,"general/misc_upload.html",{'msg':msg,'form': form})
        
        else:
            msg = "Error while uploading"
            return render(request,"general/misc_upload.html",{'msg':msg , 'form': form})


    else:
        form = MiscUpload()
    return render(request, 'general/misc_upload.html', { 'form': form , 'msg':msg})