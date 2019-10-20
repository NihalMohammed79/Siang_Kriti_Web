from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from main.models import *

class BooksUpload(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('author','title','document')

class NotesUpload(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('course','title','document')

class MiscUpload(forms.ModelForm):
    class Meta:
        model = MiscNote
        fields = ('desc','title','document')

class VideoUpload(forms.ModelForm):
    class Meta:
        model = CourseVideo
        fields = ('course','title','document')
