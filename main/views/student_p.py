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

@login_required
def student_dashboard(request):
    return render(request,'students/dashboard.html')

def student_courses(request):
    fil = CourseVideo.objects.all()
    n = Note.objects.all()
    return render(request, 'students/courses.html',{'videos':fil,'notes':n})

def student_club_courses(request):
    fil = CourseVideo.objects.all()
    n = Note.objects.all()
    return render(request, 'students/club_courses.html',{'videos':fil,'notes':n})

def student_book_upload(request):
    msg = ""
    if request.method == 'POST':
        form = BooksUpload(request.POST, request.FILES)
        if form.is_valid():
            analysis = form.save(commit=False)
            analysis.user = request.user
            if request.user.is_student:
                analysis.is_approved = 0
            else:
                analysis.is_approved = 1
            analysis.save()
            msg = "Book uploaded successfully"
            return render(request,"students/books_upload.html",{'msg':msg,'form': form})
        
        else:
            msg = "Error while uploading"
            return render(request,"students/books_upload.html",{'msg':msg , 'form': form})


    else:
        form = BooksUpload()
    return render(request, 'students/books_upload.html', { 'form': form , 'msg':msg})

def student_note_upload(request):
    msg = ""
    departments = Department.objects.all()
    if request.method == 'POST':
        form = NotesUpload(request.POST, request.FILES)
        if form.is_valid():
            analysis = form.save(commit=False)
            analysis.user = request.user
            if request.user.is_student:
                analysis.is_approved = 0
            else:
                analysis.is_approved = 1
            analysis.save()
            msg = "Notes uploaded successfully"
            return render(request,"students/notes_upload.html",{'msg':msg,'form': form , 'departments':departments})
        
        else:
            msg = "Error while uploading"
            return render(request,"students/notes_upload.html",{'msg':msg , 'form': form , 'departments':departments})


    else:
        form = NotesUpload()
    return render(request, 'students/notes_upload.html', { 'form': form , 'msg':msg , 'departments':departments})
        