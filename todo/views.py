from django.shortcuts import render, redirect


todo_database = [
    {
        'id':1,
        'todo_item': 'First todo',
    },
    {
        'id':2,
        'todo_item': 'Second todo',
    },
    {
        'id':3,
        'todo_item': 'Third todo',
    },
]

def index(request):

    context = {
        'todos': todo_database
    }

    return render(request, template_name='todo/index.html', context=context)


def add_todo(request):
    if request.method == 'POST':
        todo_item = request.POST.get('todo')

        todo_id = None
        if len(todo_database) == 0:
            todo_id = 0
        else:
            todo_id = todo_database[-1].get('id') + 1
            
        todo_database.append({
            'id': todo_id,
            'todo_item': todo_item
        })

    return render(request, template_name='todo/add.html')



def remove_add(request, todo_id):
    for todo in todo_database:
        if todo.get('id') == todo_id:
            todo_database.remove(todo)

    return redirect('index')