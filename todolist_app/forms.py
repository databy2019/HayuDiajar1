#todolist_app\forms.py
from django import forms
from todolist_app.models import TaskList

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields =['task', 'tanggal','pelajaran', 'waktu', 'cara', 'jam', 'durasi', 'nilai', 'positif', 'negatif', 'done']
