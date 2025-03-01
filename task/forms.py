
from django import forms

from task.models import Task


class Task_form(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'done']
        widgets = {
            'done': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }