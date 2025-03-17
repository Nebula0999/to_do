
from django import forms
from django.forms import ModelForm
from task.models import Task


class Task_form(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
      