from django import forms
from dashboard.models import *

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fiels = ['title', 'description']