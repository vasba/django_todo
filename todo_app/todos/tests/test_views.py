from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from todos.models import TodoItem

class TodoViewsTest(TestCase):
    
    def setUp(self):
        super().setUp()
        # Create a user for the tests
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        # Create a TodoItem for the tests
        self.todo_item = TodoItem.objects.create(title='Test Todo', description='Test Description', user=self.user)

    def test_list_todo_items(self):
        response = self.client.get(reverse('list-todos'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Todo')
        self.assertTemplateUsed(response, 'todos/todo_list.html')

    def test_add_todo_item(self):
        response = self.client.post(reverse('add_todo_item'), {'title': 'New Todo', 'description': 'New Description'})
        self.assertEqual(response.status_code, 302)  # Redirect to list-todos
        new_todo = TodoItem.objects.get(title='New Todo')
        self.assertIsNotNone(new_todo)
        self.assertEqual(new_todo.description, 'New Description')

    def test_remove_todo_item(self):
        response = self.client.get(reverse('remove_todo_item', args=[self.todo_item.id]))
        self.assertEqual(response.status_code, 302)  # Redirect to list-todos
        with self.assertRaises(TodoItem.DoesNotExist):
            TodoItem.objects.get(id=self.todo_item.id)
