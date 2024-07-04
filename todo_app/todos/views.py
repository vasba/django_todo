from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import TodoItem
from .forms import TodoItemForm

@login_required
def list_todo_items(request):
    items = TodoItem.objects.filter(user=request.user) 
    return render(request, 'todos/todo_list.html', {'items': items})

@login_required
def add_todo_item(request):
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            return redirect('list_todos')
    else:
        form = TodoItemForm()
    return render(request, 'todos/add_todo_item.html', {'form': form})

@login_required
def remove_todo_item(request, item_id):
    item = get_object_or_404(TodoItem, id=item_id, user=request.user)
    item.delete()
    return redirect('list_todos')

@login_required
def toggle_todo_item(request, item_id):
    item = get_object_or_404(TodoItem, id=item_id, user=request.user)
    item.completed = not item.completed
    item.save()
    return redirect('list_todos')