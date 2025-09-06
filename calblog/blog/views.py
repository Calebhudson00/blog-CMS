from django.shortcuts import render
from .models import Post
from django.views import generic
from django.views.decorators.http import require_GET
from django.http import HttpResponse

class PostList(generic.ListView):
  queryset=Post.objects.filter(status=1).order_by('-created_on')
  template_name='index.html'
  paginate_by = 4

class PostDetail(generic.DetailView):
  model=Post
  template_name='post.html'