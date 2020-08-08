from django.test import TestCase
from .models import Editor, Post, tags

# Create your tests here.

class EditorTestClass(TestCase):

    #Set up method
    def setUp(self):
        self.fred = Editor(first_name='Fredrick', last_name='Ojure', email='fredojure@hotmail.com')
    
    #Test save method
    def test_save_method(self):
        self.fred.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

