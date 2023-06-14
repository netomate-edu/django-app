from django.shortcuts import render


def index(request):
    todo_items = [
        'First task',
        'Second task',
        'Third task',
        'Fourth task'
    ]
    context = {
        'todos': todo_items
    }

    return render(request, template_name='todo/index.html', context=context)


def add_todo(request):

    return render(request, template_name='todo/add.html')