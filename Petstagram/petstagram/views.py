from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.apps import apps
from .models import Feed

def index(request):
    return render(request, 'petstagram/index.html')

def mypage(request):
    return render(request, 'petstagram/mypage.html')

def home(request):
    feeds = Feed.objects.all()
    return render(request, 'petstagram/index.html', {'feeds':feeds})

def detail(request, feed_id):
    feed = get_object_or_404(Feed, pk=feed_id)
    return render(request, 'petstagram/detail.html', {'feed':feed})

def new(request):
    return render(request, 'petstagram/new.html')

def create(request):
    CustomUser = apps.get_model('account', 'CustomUser')
    user = CustomUser.objects.get(username=request.user) #로그인한 유저 정보 가져오기

    new_feed = Feed()
    new_feed.title = request.POST['title']
    new_feed.author_id = user
    new_feed.author_name = user.nickname     #유저 닉네임으로 작성자 저장
    new_feed.context = request.POST['context']
    new_feed.create_date = timezone.datetime.now()
    try:
        new_feed.media = request.FILES['media']
    except:
        pass
    new_feed.save()
    return redirect('/')

def edit(request, feed_id):
    feed = get_object_or_404(Feed, pk=feed_id)
    return render(request, 'petstagram/edit.html', {'feed':feed})

def update(request, feed_id):
    edit_feed = get_object_or_404(Feed, pk=feed_id)
    edit_feed.title = request.POST['title']
    edit_feed.context = request.POST['context']
    edit_feed.create_date = timezone.datetime.now()
    try:
        edit_feed.media = request.FILES['media']
    except:
        pass
    edit_feed.save()
    return redirect('/')

def delete(request, feed_id):
    delete_feed = get_object_or_404(Feed, pk=feed_id)
    delete_feed.delete()
    return redirect('/')