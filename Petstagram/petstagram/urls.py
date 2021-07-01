from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.home, name="home"),
    path('mypage', views.mypage, name="mypage"),
    path('feed/new', views.new, name="new"),
    path('feed/create', views.create, name="create"),
    path('feed/delete/<int:feed_id>', views.delete, name="delete"),
    path('feed/edit/<int:feed_id>', views.edit, name="edit"),
    path('feed/update/<int:feed_id>', views.update, name="update"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)