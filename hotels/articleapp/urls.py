from django.urls import path
from .views import *
urlpatterns = [
    path("blog-list", ArticleListview.as_view() , name = 'blog-post')
    
]

