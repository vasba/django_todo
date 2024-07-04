from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from .models import TodoItem
from .forms import TodoItemForm

@login_required
def list_todo_items(request):
    title_query = request.GET.get('title_search', '')  # Capture title search keyword
    description_query = request.GET.get('description_search', '')  # Capture description search keyword
    items = TodoItem.objects.filter(
        Q(user=request.user) & 
        Q(title__icontains=title_query) & 
        Q(description__icontains=description_query)
    ).order_by('completed')
    return render(request, 'todos/todo_list.html', {
        'items': items,
        'title_query': title_query,
        'description_query': description_query
    })

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
