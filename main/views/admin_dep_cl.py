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
def department_dashboard(request):
    return render(request,'departments/dashboard.html')


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

def book_approval(request):

    if request.method == "POST":
        iden = int(request.POST.get('extra_id'))
        ibook = int(request.POST.get('tr_id'))
        ibn = request.POST.get('bn')
        print(iden)
        print(ibook)
        print(ibn)
        if ibn == "book":
            book = Book.objects.filter(id=ibook).first()
            if iden == 1:
                book.is_approved = 1
            else:
                book.is_approved = -1
            book.save()
        return HttpResponse(iden)

    else:
        book = Book.objects.all()
        return render(request,'departments/book_approval.html',{'books':book})

def note_approval(request):

    if request.method == "POST":
        iden = int(request.POST.get('extra_id'))
        ibook = int(request.POST.get('tr_id'))
        ibn = request.POST.get('bn')
        
        if ibn == "note":
            note = Note.objects.filter(id=ibook).first()
            if iden == 1:
                note.is_approved = 1
            else:
                note.is_approved = -1
            note.save()
        return HttpResponse(iden)

    else:
        note = Note.objects.all()
        return render(request,'departments/note_approval.html',{'notes':note})

def admin_dashboard(request):
    return render(request,'admin/dashboard.html')