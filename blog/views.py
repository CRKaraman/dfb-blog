# posts/views.py

from django.views.generic import ListView, DetailView # new

from .models import Post

class BlogListView(ListView):
  model = Post
  template_name = 'home.html'
  context_object_name = 'all_posts_list' # new

class BlogDetailView(DetailView): # new
  model = Post
  template_name = 'post_detail.html'