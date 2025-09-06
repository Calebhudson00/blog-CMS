from . import views
from django.urls import path
from .views import *

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('post/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('post/<slug:slug>/amp/', PostAMPDetail.as_view(), name='post_detail_amp'),
]
