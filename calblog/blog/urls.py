from . import views
from django.urls import path
from .views import PostList, PostDetail
from .feed import blogFeed

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('post/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('feed/', blogFeed(), name='post_feed'),
]
