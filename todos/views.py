from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .form import TodoForm
from .models import Todo
# Create your views here.
def todo_home(request):
    queryset = Todo.objects.all()

    context = {
        "form": queryset
    }
    return  render(request, "home.html", context)
def todo_details(request, id):
    queryset = Todo.objects.get(id=id)

    context = {
        "form": queryset
    }
    return render(request, "details.html",context)

def todo_add(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TodoForm()


    context = {
        "form": form
    }
    return render(request, "add_todo.html",context)

def todo_delete(request, id):
    form = get_object_or_404(Todo, id=id)
    if request.method == "POST":
        form.delete()
        redirect('/todos')

    context = {
        "form": form
    }
    return render(request, "add_todo.html",context)

def todo_edit(request, id):
    form = get_object_or_404(Todo, id=id)
    form = TodoForm
    # form.text = TodoForm.text.data
    if request.method == "POST":
        form.save()
        redirect('/todos')

    context = {
        "form": form
    }
    return render(request, "add_todo.html",context)
