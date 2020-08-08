from django.test import TestCase
from .models import Editor, Post, tags

import datetime as dt

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
    
        #Create a new tag and save it
        self.new_tag = tags(name='testing')
        self.new_tag.save()

        self.new_post = Post(title='Test Post', post='This is a random test Post', editor=self.fred)
        self.new_post.save()

        self.new_post.tags.add(self.new_tag)
    
    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
    
    def test_get_post_today(self):
        posts_today = Post.today_posts()
        self.assertTrue(len(post_today) > 0)
    
    def test_get_post_by_date(self):
        test_date = '2020-07-25'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        post_by_date = Post.days_post(date)
        self.assertTrue(len(post_by_date) == 0)



