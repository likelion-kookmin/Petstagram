from django.shortcuts import render, get_object_or_404, redirect
from .models import Feed

def index(request):
    return render(request, 'petstagram/index.html')

def home(request):
    feeds = Feed.objects.all()
    return render(request, 'petstagram/index.html', {'feeds':feeds})

def detail(request, feed_id):
    feed = get_object_or_404(Feed, pk=feed_id)
    return render(request, 'petstagram/detail.html', {'feed':feed})

def new(request):
    return render(request, 'petstagram/new.html')

def create(request):
    new_feed = Feed()
    new_feed.title = request.POST['title']
    new_feed.text = request.POST['text']
    new_feed.save()
    return redirect('/')

def delete(request, feed_id):
    delete_feed = get_object_or_404(Feed, pk=feed_id)
    delete_feed.delete()
    return redirect('/')