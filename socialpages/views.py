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

def search_results(request):

    if 'post' in request.GET and request.GET['post']:
        search_term = request.GET.get('post')
        searched_posts = Post.search_by_title(search_term)
        message = f"{search_term}"
        
        context = {'message': message, 'posts': searched_posts}
        return render(request, 'all-social/search.html', context)
    
    else:
        message = "You haven't searched for any term"
        context = {'message': message}
        return render(request, 'all_social/search.html', context)

def post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except DoesNotExist:
        raise Http404()

    context = {"post": post}
    return render(request, 'all-social/post.html', context)