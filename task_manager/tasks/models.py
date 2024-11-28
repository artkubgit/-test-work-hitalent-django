from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Низкий'),
        ('medium', 'Средний'),
        ('high', 'Высокий'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Не выполнена'),
        ('completed', 'Выполнена'),
    ]

    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    category = models.CharField(max_length=100, verbose_name="Категория")
    due_date = models.DateField(verbose_name="Срок выполнения")
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, verbose_name="Приоритет")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name="Статус")

    def __str__(self):
        return self.title
