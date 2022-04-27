from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView,DetailView,UpdateView
from .models import *
# Create your views here.
class ArticleListview(ListView):
    model = ArticleModel
    template_name = "articleapp/blog-list.html"
    
class ArticleDetailviews(DetailView):
    model = ArticleModel
    template_name = "articleapp/blog-detail.html"
    
    
class ArticleCreate(CreateView):
    model = ArticleModel
    template_name = "articleapp/blog-create.html"
    
    fields = "__all__"
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        
        
    
    
class ArticleUpdateview(UpdateView):
    model = ArticleModel
    template_name = "articl"
