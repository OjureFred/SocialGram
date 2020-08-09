from django.db import models
import datetime as dt

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    handle = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank = True)

    def __str__(self):
        return self.first_name
    
    def save_editor(self):
        self.save()
    class Meta:
        ordering = ['first_name']

class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=60)
    post = models.TextField()
    editor = models.ForeignKey(Editor, on_delete = models.DO_NOTHING)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(upload_to = 'posts/')

    def __str__(self):
        return self.title
    
    @classmethod
    def today_posts(cls):
        today = dt.date.today()
        posts = cls.objects.filter(pub_date=today)
        return posts
    
    @classmethod
    def days_post(cls, date):
        posts = cls.objects.filter(pub_date=date)
    
    @classmethod
    def search_by_title(cls, search_term):
        posts = cls.objects.filter(title__icontains=search_term)
        return posts
