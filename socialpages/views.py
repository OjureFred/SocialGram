from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

# Other imports

# Create your views here.
def main_page(request):
    date = dt.date.today()
    context = {'date': date,}
    return render(request, 'main_page.html', context)
