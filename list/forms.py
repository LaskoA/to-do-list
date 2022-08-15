from .models import Task
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            'date': DateInput(),
            'deadline': DateInput()
        }
