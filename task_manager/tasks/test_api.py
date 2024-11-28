from rest_framework.test import APITestCase
from rest_framework import status
from .models import Task

class TaskAPITest(APITestCase):

    def setUp(self):
        self.task_data = {
            "title": "Тестирование REST API",
            "description": " Django REST Framework",
            "category": "API",
            "due_date": "2024-12-10",
            "priority": "high",
            "status": "pending"
        }
        self.task = Task.objects.create(**self.task_data)

    def test_get_tasks(self):
        """Проверяем, что задачи возвращаются корректно."""
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_task(self):
        """Проверяем создание новой задачи через API."""
        new_task = {
            "title": "Тестирование REST API 2",
            "description": "Понять, как тестировать REST API",
            "category": "Работа",
            "due_date": "2024-12-15",
            "priority": "medium",
            "status": "pending"
        }
        response = self.client.post('/api/tasks/', new_task)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)
