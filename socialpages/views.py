from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import datetime as dt

# Other imports
from .models import Post, PostRecipients
from .forms import PostForm, NewPostForm
from .email import send_welcome_email

# Create your views here.
def main_page(request):
    date = dt.date.today()
    all_posts = Post.objects.all()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = PostRecipients(name=name, email=email)
            recipient.save()
            send_welcome_email(name, email)

            HttpResponseRedirect('main_page')
    else:
        form = PostForm()

    context = {'date': date, 'all_posts': all_posts, 'postForm': form}
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

@login_required(login_url='/accounts/login/')
def post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except DoesNotExist:
        raise Http404()

    context = {"post": post}
    return render(request, 'all-social/post.html', context)

@login_required(login_url='/accounts/login')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.editor = current_user
            post.save()
        return redirect('main_page')
    
    else:
        form = NewPostForm()
    
    context = {"form": form}
    return render(request, 'new_post.html', context)