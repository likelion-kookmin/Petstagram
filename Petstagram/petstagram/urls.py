from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.home, name="home"),
    path('feed/new', views.new, name="new"),
    path('feed/create', views.create, name="create"),
] 