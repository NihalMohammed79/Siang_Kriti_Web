from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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
from django.db import connection
import datetime

@department
def department_dashboard(request):
    courses = Course.objects.filter(department=request.user.department).all()
    vcount = 0
    ncount = 0 
    for course in courses:
        v = CourseVideo.objects.filter(course=course).count()
        n = Note.objects.filter(course=course,is_approved=1).count()
        vcount += int(v)
        ncount += int(n)
    bcount = Book.objects.filter(is_approved=1).count()
    return render(request,'departments/dashboard.html',{'vcount':vcount , 'ncount':ncount ,'bcount':bcount , 'courses':courses})

@club
def club_dashboard(request):
    courses = Course.objects.filter(department=request.user.department).all()
    vcount = 0
    ncount = 0 
    for course in courses:
        v = CourseVideo.objects.filter(course=course).count()
        n = Note.objects.filter(course=course,is_approved=1).count()
        vcount += int(v)
        ncount += int(n)
    bcount = Book.objects.filter(is_approved=1).count()
    return render(request,'clubs/dashboard.html',{'vcount':vcount , 'ncount':ncount ,'bcount':bcount , 'courses':courses})

@no_student
def video_upload(request):
    msg = ""
    departments = Department.objects.all()
    if request.method == 'POST':
        form = VideoUpload(request.POST, request.FILES)
        if form.is_valid():
            analysis = form.save(commit=False)
            analysis.user = request.user
            analysis.save()
            msg = "Video uploaded successfully"
            return render(request,"general/video_upload.html",{'msg':msg,'form': form , 'departments':departments})
        
        else:
            msg = "Error while uploading"
            return render(request,"general/video_upload.html",{'msg':msg , 'form': form , 'departments':departments})


    else:
        form = VideoUpload()
    return render(request, 'general/video_upload.html', { 'form': form , 'msg':msg , 'departments':departments})

@admin
def book_approval(request):

    if request.method == "POST":
        iden = int(request.POST.get('extra_id'))
        ibook = int(request.POST.get('tr_id'))
        ibn = request.POST.get('bn')
        # print(iden)
        # print(ibook)
        # print(ibn)
        if ibn == "book":
            book = Book.objects.filter(id=ibook).first()
            if iden == 1:
                book.is_approved = 1
                book.user.contri += 1
            else:
                book.is_approved = -1
            book.save()
        return HttpResponse(iden)

    else:
        book = Book.objects.all()
        return render(request,'departments/book_approval.html',{'books':book})

@no_student
def note_approval(request):

    if request.method == "POST":
        iden = int(request.POST.get('extra_id'))
        ibook = int(request.POST.get('tr_id'))
        ibn = request.POST.get('bn')
        
        if ibn == "note":
            note = Note.objects.filter(id=ibook).first()
            if iden == 1:
                note.is_approved = 1
                note.user.contri += 1
            else:
                note.is_approved = -1
            note.save()
        return HttpResponse(iden)

    else:
        note = Note.objects.all()
        return render(request,'departments/note_approval.html',{'notes':note})

@admin
def misc_approval(request):

    if request.method == "POST":
        iden = int(request.POST.get('extra_id'))
        ibook = int(request.POST.get('tr_id'))
        ibn = request.POST.get('bn')
        
        if ibn == "misc":
            misc = MiscNote.objects.filter(id=ibook).first()
            if iden == 1:
                misc.is_approved = 1
                misc.user.contri += 1
            else:
                misc.is_approved = -1
            misc.save()
        return HttpResponse(iden)

    else:
        misc = MiscNote.objects.all()
        return render(request,'admin/misc_approval.html',{'miscs':misc})

@admin
def add_dept(request):
    msg = ""
    if request.method == 'POST':
        form = AddDept(request.POST, request.FILES)
        if form.is_valid():
            analysis = form.save(commit=False)
            analysis.save()
            msg = "Added successfully"
            return render(request,"admin/add_dept.html",{'msg':msg,'form': form})
        
        else:
            msg = "Error while adding"
            return render(request,"admin/add_dept.html",{'msg':msg , 'form': form})


    else:
        form = AddDept()
    return render(request, 'admin/add_dept.html', { 'form': form , 'msg':msg})

@no_student
def add_course(request):
    msg = ""
    if request.method == 'POST':
        form = AddCourse(request.POST, request.FILES)
        if form.is_valid():
            analysis = form.save(commit=False)
            analysis.department = request.user.department
            analysis.save()
            msg = "Added successfully"
            return render(request,"departments/add_course.html",{'msg':msg,'form': form})
        
        else:
            msg = "Error while adding"
            return render(request,"departments/add_course.html",{'msg':msg , 'form': form})


    else:
        form = AddCourse()
    return render(request, 'departments/add_course.html', { 'form': form , 'msg':msg})

@admin
def admin_dashboard(request):
    bcount = Book.objects.filter(is_approved=1).count()
    ncount = Note.objects.filter(is_approved=1).count()
    vcount = CourseVideo.objects.count()
    depts = Department.objects.all()
    return render(request,'admin/dashboard.html',{'vcount':vcount , 'ncount':ncount ,'bcount':bcount , 'depts':depts})

