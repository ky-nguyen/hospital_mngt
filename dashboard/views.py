from django.shortcuts import render
from dashboard.models import Notes
from dashboard.forms import *
# Create your views here.


def home(request):
    return render(request, 'dashboard/home.html')


def notes(request):
    form = NotesForm()
    notes = Notes.objects.filter(user=request.user)
    context = {
        'notes': notes,
        'form': form
    }
    return render(request, 'dashboard/notes.html', context) 