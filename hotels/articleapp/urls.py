from django.urls import path
from .views import *
urlpatterns = [
    path("blog-list/", ArticleListview.as_view() , name = 'blog-post'),
    path("blog-detail/<int:pk>", ArticleDetailviews.as_view(), name = 'blog-detail'),
    path("blog-create/", ArticleCreate.as_view(),name="blog-create"),
]

