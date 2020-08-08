from django.shortcuts import render
from django.http import HttpResponse

# Other imports

# Create your views here.
def main_page(request):
    return render(request, 'main_page.html')
