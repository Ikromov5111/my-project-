from time import time
from django.shortcuts import render , redirect

from config.settings import EMAIL_HOST
from.forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# sariq dev
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView, DeleteView
# from .models import Article

from django.core.mail import send_mail
from django.core.mail import *

#sariqdev funksiyalari
# class ArticleListView(ListView):
#     model = Article
#     template_name = 'mainapp/blog-post'
#     context={}
# def aticleList(request):
#     articles = Article.objects.all()
#     context = {
        
#         "articles" : articles
#     }
#     return render(request, 'mainapp/blog-post.html', context)

# def article_c(request):
#     form = ArticleForm()
#     if request.method == "POST":
#         form = ArticleForm(request.POST)
#         if form.is_valid:
#             form.save()
#             return redirect('blog_post')
        
#     context = {
#         "form" : form
#     }
#     return render(request,'mainapp/article_post.html', context)

# def article_u(request,pk):
#     article = Article.objects.get(id=pk) 
#     form = ArticleForm(instance=article) 
#     if request.method == "POST":
#         form = ArticleForm(instance=article)
#         if form.is_valid:
#             form.save()
#             return redirect('blog_post')
        
#     context = {
#         "form" : form 
#     }
#     return render(request,'mainapp/article_post.thml',context)
# # Create your views here.
# def  article_d(request,pk):
#     article = Article.objects.get(id=pk)
#     if request.method == "POST":
#         article.delete()
        
#     context = {
#         "article" : article
#     }
#     return render(request,"mainapp/test.html", context)
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('mainpage')
    else:  
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get('password') 
            user = authenticate(request,username = username , password = password)
            if user is not None:
                login(request,user)
                return redirect('mainpage')
            else:
                messages.info(request,"qandaydir Xatolik")
        context= {}
        return render(request,'mainapp/login.html', context)


def logoutuser(request):
    logout(request)
    return redirect('login')

def registerUser(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        EMAIL_HOST = request.POST.get("email")
        send_mail(
        'Diamond mehmonhonasi',
        "Mehmonxonamizdan ro'yxatdan o'tganiz bilan tabrikliman.",
        'javohirikromov003.com',
        [EMAIL_HOST],
        fail_silently=False,)
        if form.is_valid():
           
            form.save()
            
            user = form.cleaned_data.get('username')
            return redirect('login')
        
    context = {
        "form" : form
    }
    return render(request,'mainapp/register.html', context)


def profil(request):
    if request.user.is_superuser:
        form = HotelForm()
        if request.method == "POST":
            form = HotelForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('mainpage')
        
        context = {
            "form" : form
        }
    
        return render(request,"mainapp/frofile.html",context)  
    else:
        return redirect('mainpage')

def worker_table(request):
    workers = Worker.objects.all().order_by("added_time")
    context = {
        "workers" : workers
    }
    
    return render(request, 'mainapp/worker_table.html', context)

def worker_create(request):
    if request.user.is_superuser:
        form = WorkerForm()
        if request.method == "POST":
            form = WorkerForm(request.POST)
            if form.is_valid:
                form.save()
                return redirect('worker_t')
        context = {
            "form":form
        }
        return render(request,"mainapp/worker_create.html",context)
    else:
        return redirect('mainpage')
    
def worker_update(request,pk):
    if request.user.is_superuser:
        worker = Worker.objects.get(id = pk)
        form = WorkerForm(instance=worker)
        if request.method == "POST":
            form = WorkerForm(request.POST, instance=worker)
            if form.is_valid:
                form.save()
                return redirect('worker_t')
        
        context = {
            "form" : form
        }
        return render(request,"mainapp/worker_create.html", context)
    else :
        return redirect('mainpage')

def worker_delete(request,pk):
    if request.user.is_superuser:
        worker = Worker.objects.get(id = pk)
        if request.method == "POST":
            worker.delete()
            return redirect('worker_t')
        
        context = {
            "worker" : worker
        }
        return render(request, "mainapp/delete.html",context)
    else :
        return redirect("mainpage")
    

def rooms_see(request):
    if request.user.is_superuser:
        rooms = Room.objects.all().order_by("number")
        context = {
            
            "rooms" : rooms
        }
        return render(request,'mainapp/room.html', context)
    else :
        return redirect('mainpage')

def room_c(request):
    image = 'file' in request.FILES and request.FILES['file'] 
    form = RoomCreateForm()
    if request.method == "POST":
        form = RoomCreateForm(request.POST)
        form.photo = image
        if form.is_valid:
            form.save()
            return redirect('room_s')
        
    context = {
        "form" : form
    } 
    return render(request,'mainapp/room_create.html', context)

def room_u(request,pk):
    room = Room.objects.get(id = pk)
    form = RoomCreateForm(instance=room)
    if request.method =="POST":
        form = RoomCreateForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_s')
        
    context = {
        "form":form
    }
    
    return render(request, 'mainapp/room_create.html',context)
    
def room_d(request,pk):
    room = Room.objects.get(id=pk) 
    if request.method == "POST":
        room.delete()
        
    context ={
        "room" : room
    }       
    return render(request,"mainapp/test.html", context)

    
def mainpage(request):
    return render(request,'mainapp/index.html')
def temp(request):
    return render(request,'mainapp/temp.html')
def about(request):
    return render(request,'mainapp/about.html')
def accomodation(request):
    return render(request,'mainapp/accomodation.html')
def  blogsingle(request):
    return render(request,'mainapp/blog-single.html')
def blog(request):
    return render(request,'mainapp/blog.html')
def contact(request):
    return render(request,'mainapp/contact.html')
def  elements(request):
    return render(request,'mainapp/elements.html')
def gallery(request):
    return render(request,'mainapp/gallery.html')

def blog_post(request):
    return render(request, 'mainapp/blog-post.html')

def test(request):
    return render(request,'mainapp/test.html')




