from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views 
from django.conf.urls import include
from django.views.generic.base import RedirectView
from main.decorators import *

urlpatterns = [
		
		path('', views.index, name='index'),
		path('student', views.student_dashboard, name='student_dashboard'),
		path('student/book/upload', views.student_book_upload, name='student_book_upload'),
		path('login', views.events_login, name='events_login'),
		path('redirect', views.redirect_ac, name='redirect'),
		path('logout/', views.logout_view, name='logout'),

]