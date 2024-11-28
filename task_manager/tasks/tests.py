from django.test import TestCase
from .models import Task

class TaskModelTest(TestCase):

    def setUp(self):
        Task.objects.create(
            title="Написать тесты",
            description="Тесты для модели Task",
            category="Работа",
            due_date="2024-12-01",
            priority="medium",
            status="pending"
        )

    def test_task_creation(self):
        """Проверяем, что задача создается корректно."""
        task = Task.objects.get(title="Написать тесты")
        self.assertEqual(task.category, "Работа")
        self.assertEqual(task.priority, "medium")
        self.assertEqual(task.status, "pending")

    def test_task_str(self):
        """Проверяем метод __str__."""
        task = Task.objects.get(title="Написать тесты")
        self.assertEqual(str(task), "Написать тесты")
