from django import forms
from .models import Routine, ToDo

class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ['name']

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['description']
