from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from main.models import *

class BooksUpload(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('author','title','document')
