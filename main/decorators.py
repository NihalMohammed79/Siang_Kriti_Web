from .models import *
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect



def admin(function):
    def wrapper(request, *args, **kwargs):
        user=request.user
        if user.is_authenticated:
            if user.is_admin:
                return function(request, *args, **kwargs)
            else:
                return redirect("/")           
        else:
            return redirect("/login")
    return wrapper

def department(function):
    def wrapper(request, *args, **kwargs):
        user=request.user
        if user.is_authenticated:
            if user.is_department:
                return function(request, *args, **kwargs)
            else:
                return redirect("/")           
        else:
            return redirect("/login")
    return wrapper

def club(function):
    def wrapper(request, *args, **kwargs):
        user=request.user
        if user.is_authenticated:
            if user.is_club:
                return function(request, *args, **kwargs)
            else:
                return redirect("/")           
        else:
            return redirect("/login")
    return wrapper

def no_student(function):
    def wrapper(request, *args, **kwargs):
        user=request.user
        if user.is_authenticated:
            if user.is_club or user.is_department or user.is_admin:
                return function(request, *args, **kwargs)
            else:
                return redirect("/")           
        else:
            return redirect("/login")
    return wrapper

def student(function):
    def wrapper(request, *args, **kwargs):
        user=request.user
        if user.is_authenticated:
            if user.is_student:
                return function(request, *args, **kwargs)
            else:
                return redirect("/")           
        else:
            return redirect("/login")
    return wrapper