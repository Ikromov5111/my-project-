from tkinter.tix import Form
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView,DetailView,UpdateView
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class ArticleListview(ListView):
    model = ArticleModel
    template_name = "articleapp/blog-list.html"
    
class ArticleDetailviews(DetailView):
    model = ArticleModel
    template_name = "articleapp/blog-detail.html"
    
    
class ArticleCreate(CreateView,Form):
    model = ArticleModel
    template_name = "articleapp/blog-create.html"
    
    
        
    fields = "__all__"
    
    
        
    
        
        
    
    
class ArticleUpdateview(UpdateView):
    model = ArticleModel
    template_name = "articl"
