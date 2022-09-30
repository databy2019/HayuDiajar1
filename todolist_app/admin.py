from django.contrib import admin
#from .models import TaskList
from todolist_app.models import TaskList

class TaskListAdmin(admin.ModelAdmin):
    list_display = ('id','task', 'tanggal', 'pelajaran', 'waktu', 'cara', 'jam', 'durasi', 'nilai', 'positif', 'negatif', 'done', 'owner')

admin.site.register(TaskList, TaskListAdmin)

#admin.site.register(TaskList)
