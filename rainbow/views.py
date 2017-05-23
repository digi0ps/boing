from django.shortcuts import render
from rainbow.models import story

# Create your views here.


def home(request):
    return render(request, 'home.html')


def fluff(request):
    stories = story.objects.all().order_by('-createdTime')
    return render(request, 'fluff.html', {'stories': stories, })
