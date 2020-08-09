from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

# Other imports
from .models import Post

# Create your views here.
def main_page(request):
    date = dt.date.today()
    all_posts = Post.objects.all()
    context = {'date': date, 'all_posts': all_posts}
    return render(request, 'main_page.html', context)
