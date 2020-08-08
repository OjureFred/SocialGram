from django.shortcuts import render
from django.http import HttpResponse

# Other imports

# Create your views here.
def main_page(request):
    return HttpResponse('Welcome to SocialGram. Where you share your stories as they unfold')
