from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required


def index(request):
    posts = Post.objects.filter(user_id = request.user.id).order_by('id').reverse()
    top_posts = Post.objects.all().order_by("-likes")
    recent_posts = Post.objects.all().order_by("-id")
    user = request.user
    media_url = settings.MEDIA_URL
    
    context = {
        'posts': posts,
        'top_post':top_posts,
        'recent_posts': recent_posts,
        'user':user,
        'media_url':media_url
    }
    return render(request, 'index.html', context)

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('blogs:signup')
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect('blogs:signup')
            else:
                User.objects.create_user(username=username, email=email, password=password).save()
                return redirect('blogs:signin')
        else:
            messages.info(request, "Password should match")
            return redirect('blogs:signup')
    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("blogs:index")
        else:
            messages.info(request, "Username or Password is incorrect")
            return redirect("blogs:signin")
    return render(request, 'signin.html')
        
def logout(request):
    auth.logout(request)
    return redirect('blogs:index')

def create(request):
    if request.method == 'POST':
        postname = request.POST['postname']
        content = request.POST['content']
        category = request.POST['category']
        image = request.FILES['image']
        Post(postname=postname, content=content, category=category, 
             image=image, user = request.user).save()
        return redirect('blogs:index')
    else:
        return render(request, 'create.html')
    
def increaselikes(request,id):
    post=Post.objects.get(id=id)
    post.likes+=1
    post.save()
    return redirect("blogs:index")

def editpost(request, post_id):
    post = Post.objects.get(id = post_id)
    if request.method == "POST":
        try:
            postname = request.POST['postname']
            content = request.POST['content']
            category = request.POST['category']
            
            post.postname = postname
            post.content = content
            post.category = category
            post.save()
        except:
            print("Something went wrong")
        return redirect("blogs:index")
    return render(request, "editpost.html", {"post":post})

def delete_post(request, post_id):
    post =Post.objects.get(id=post_id)
    post.delete()
    return redirect('blogs:index') 
 