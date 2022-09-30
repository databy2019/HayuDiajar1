#todolist_app\views.py
from turtle import window_height
from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required

import pandas as pd
from plotly.offline import plot
import plotly.express as px
from plotly.graph_objs import Scatter
import plotly.graph_objects as go


@login_required
def todolist(request):
    if request.method== "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            #form.save(commit=False).owner = request.user
            #form.save()
            #atau
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
        messages.success(request,("Kegitan baru ditambahkan!"))
        return redirect('todolist')
    else:
        #all_task = TaskList.objects.all() --jik menampilkan semua data siapa aja
        all_task = TaskList.objects.filter(owner=request.user).order_by('id').reverse()
        page = request.GET.get('page', 1)
        paginator = Paginator(all_task, 10)
        try:
            all_tasks = paginator.page(page)
        except PageNotAnInteger:
            all_tasks = paginator.page(1)
        except EmptyPage:
            all_tasks = paginator.page(paginator.num_pages)

        return render(request, 'todolist.html', { 'all_tasks': all_tasks })

@login_required
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.owner == request.user:
        task.delete()
    else:
        messages.error(request, ("Akses dilarang, Anda tidak diperbolehkan"))

    return redirect('todolist')
    
@login_required
def edit_task(request, task_id):
    if request.method== "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance = task)
        if form.is_valid():
            form.save()

        messages.success(request,("Kegiatan berhasil di edit!"))
        return redirect('todolist')
    else:
        task_obj = TaskList.objects.get(pk=task_id)

        return render(request, 'edit.html',{'task_obj': task_obj })

@login_required
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.owner == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request, ("Akses dilarang, Anda tidak diperbolehkan"))
    
    return redirect('todolist')

@login_required
def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.owner == request.user:
        task.done = False
        task.save()
    else:
        messages.error(request, ("Akses dilarang, Anda tidak diperbolehkan"))
        
    return redirect('todolist')

def contact(request):
    context ={
        'contact_text' : "",
    }
    return render(request, 'contact.html', context)

@login_required
def hasil(request):
    #all_task = TaskList.objects.all() --jik menampilkan semua data siapa aja
    all_task = TaskList.objects.filter(owner=request.user).order_by('id').reverse()
    page = request.GET.get('page', 1)
    paginator = Paginator(all_task, 10)
    try:
        all_tasks = paginator.page(page)
    except PageNotAnInteger:
        all_tasks = paginator.page(1)
    except EmptyPage:
        all_tasks = paginator.page(paginator.num_pages)

    return render(request, 'hasil.html', { 'all_tasks': all_tasks })
    
@login_required
def grafik(request):
    #all_task = TaskList.objects.all() --jik menampilkan semua data siapa aja
    all_task = TaskList.objects.filter(owner=request.user).order_by('id').reverse()
    page = request.GET.get('page', 1)
    paginator = Paginator(all_task, 10)
    try:
        all_tasks = paginator.page(page)
    except PageNotAnInteger:
        all_tasks = paginator.page(1)
    except EmptyPage:
        all_tasks = paginator.page(paginator.num_pages)

    return render(request, 'grafik.html', { 'all_tasks': all_tasks })

def index(request):
    context ={
        'index_text' : "Welcome to Index Page",
    }
    return render(request, 'index.html', context)

@login_required
def grafik(request):
    #qs = TaskList.objects.all().filter(pelajaran="Biologi1")
    qs = TaskList.objects.all()
    projects_data = [
        {
            'y_data': x.nilai,
            'x_data': x.pelajaran,
            'cara' : x.cara,
            'waktu' : x.waktu,
            'durasi' :x.durasi,
            'Responsible': x.owner.username
        } for x in qs
    ]

    df = pd.DataFrame(projects_data)
    
    ''' fig = px.line(df, x="x_data", y="y_data", 
                  labels={
                     "x_data": "ID",
                     "y_data": "Nilai",
                 }, color="cara",
                  title = "Grafik Belajar Biologi") '''

    fig = go.Figure(px.scatter(
        df, x="cara", y="y_data", height=400, width=600,
        color="x_data", labels={
                     "x_data": "Cara",
                     "y_data": "Nilai",
                     "cara" : "Mata Pelajaran",
                 }, title="Grafik Belajar menurut Cara "))
    
    fig1 = go.Figure(px.scatter(
        df, x="waktu", y="y_data", height=400, width=600,
        color="x_data", labels={
                     "x_data": "Waktu",
                     "y_data": "Nilai",
                     "waktu" : "Waktu belajar",
                 }, title="Grafik Belajar menurut Waktu "))
    
        
    fig2 = go.Figure(px.scatter(
        df, x="durasi", y="y_data", height=400, width=600,
        color="x_data", labels={
                     "x_data": "Waktu",
                     "y_data": "Nilai",
                     "durasi" : "Durasi belajar",
                 }, title="Grafik Belajar menurut Durasi waktu belajar "))
    
    #fig.update_yaxes(autorange="reversed")
    line_plot = plot(fig, output_type="div")
    line_plot2 = plot(fig1, output_type="div")
    line_plot3 = plot(fig2, output_type="div")
    
    context = {'plot_div': line_plot, 'plot_div2': line_plot2, 'plot_div3': line_plot3, }
       
    return render(request, 'grafik.html', context)
