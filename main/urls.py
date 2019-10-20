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
		path('student/note/upload', views.student_note_upload, name='student_note_upload'),
		path('student/courses', views.student_courses, name='student_courses'),
		path('student/club/courses', views.student_club_courses, name='student_club_courses'),
		path('department', views.department_dashboard, name='department_dashboard'),
		path('admind', views.admin_dashboard, name='admin_dashboard'),
		path('club', views.club_dashboard, name='club_dashboard'),
		path('book/approval', views.book_approval, name='book_approval'),
		path('note/approval', views.note_approval, name='note_approval'),
		path('misc/approval', views.misc_approval, name='misc_approval'),
		path('add/dept', views.add_dept, name='add_dept'),
		path('add/course', views.add_course, name='add_course'),
		path('misc/upload', views.misc_upload, name='misc_upload'),
		path('video/upload', views.video_upload, name='video_upload'),
		path('api/courses',views.get_courses, name='api_courses'),
		path('login', views.events_login, name='events_login'),
		path('redirect', views.redirect_ac, name='redirect_ac'),
		path('logout/', views.logout_view, name='logout'),

]