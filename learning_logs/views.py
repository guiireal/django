from django.shortcuts import render
from .models import Topic

def index(request):
    return render(request, 'learning_logs/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_add')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)
