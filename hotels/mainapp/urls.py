from django.urls import path 
from . import views


urlpatterns = [
    path("", views.mainpage , name = "mainpage" ),
    path("test/", views.temp, name= "temp" ),
    path("about/", views.about, name = "about"),
    path("accomodation/", views.accomodation, name = "accomodation"),
    path("blog-single/", views.blogsingle , name = "blog-single"),
    path("blog/", views.blog , name = "blog"),
    path("contact/", views.contact, name = "contact"),
    path("elements/" , views.elements , name = "elements"),
    path("gallery/", views.gallery, name = "gallery"),
    
    
    path("login/", views.loginUser, name = "login"),
    path('logout/', views.logoutuser, name = "logout"),
    path("register/", views.registerUser, name = "register"),
    
    
    path('profil/', views.profil, name = "profil"),
    
    path('worker_t/', views.worker_table, name = 'worker_t'),
    path('worker_c/',views.worker_create, name = 'worker_c'),
    path("worker_u/<str:pk>", views.worker_update, name = 'worker_u'),
    path("worker/<str:pk>", views.worker_delete, name = "worker_d"),
    
    path("room_s/", views.rooms_see, name = "room_s"),
    path("room_create", views.room_c, name = "room_c"),
    #saridev pathlari
   # path('article', views.articleList, name = 'article_list')
   
#    path("blog-post/", views.aticleList , name ="blog_post"),
#    path("blog_c/", views.article_c,name="blog_c"),
   path("testirov/", views.test , name ="testtirov"),
]