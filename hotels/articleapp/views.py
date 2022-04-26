from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView
from .models import *
# Create your views here.
class ArticleListview(ListView):
    model = ArticleModel
    template_name = "articleapp/blog-list.html"
    

