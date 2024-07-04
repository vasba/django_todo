"""
URL configuration for todo_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from todos.views import list_todo_items, add_todo_item, remove_todo_item

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_todo_items, name='list_todos'),
    path('add/', add_todo_item, name='add_todo_item'),  # New URL for adding todo items
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),  # Include default auth URL
    path('remove_todo_item/<int:item_id>/', remove_todo_item, name='remove_todo_item'),
]
