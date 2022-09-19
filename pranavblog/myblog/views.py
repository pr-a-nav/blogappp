

from tokenize import PseudoExtras
from django.http import HttpResponse, request
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView

from .models import Post
from .forms import Postform


# Create your views here.
# context{list=[Post]}

class HomeView(ListView):
     model = Post
     template_name = 'home.html'

class ArticleDetailview(DetailView):
    model = Post
    template_name= 'article.html'

class Postblog(CreateView):
    model = Post
    form_class=Postform
    template_name = 'add_post.html'
    # fields= '__all__'

class Updatepost(UpdateView):
    model = Post
    form_class=Postform
    template_name='update_post.html'
    # fields= ['title','body']
