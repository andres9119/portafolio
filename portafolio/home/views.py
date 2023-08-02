from django.shortcuts import render
import datetime


def home(request):
    year = datetime.datetime.now().year
    context = {'year': year}
    return render(request, 'home.html', context)
