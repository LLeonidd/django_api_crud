from django.test import TestCase
from .models import Todo


class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='TestTask', body='TestBody')

    def test_title_content(self):
        todo = Todo.objects.first()
        excpected_title = f"{todo.title}"
        self.assertEqual(excpected_title, 'TestTask')

    def test_body_content(self):
        todo = Todo.objects.first()
        excpected_title = f"{todo.body}"
        self.assertEqual(excpected_title, 'TestBody')