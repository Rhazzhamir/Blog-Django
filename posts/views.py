from django.shortcuts import render , redirect
from posts.models import Post
from posts.models import Category
from django.contrib.auth.models import User
from django.utils.text import slugify
from posts.forms import postForm
# Create your views here.

def index(request):
    post = Post.objects.all()
    category = Category.objects.all()
    author = User.objects.filter(is_superuser = True).first()
    context ={
        'posts': post,
        'categories': category,
        'authors': author,
    }

    return render(request , 'index.html' , context)

def post(request , slug):
    post = Post.objects.get(slug=slug)
    context =  {
        'post' : post,
    }
    return render(request , 'post.html' , context)

def newpost(request):
    form = postForm()
    category = Category.objects.all()
    
    if request.method == 'POST':
        category = request.POST.get('category')
        title = request.POST.get('title')
        intro = request.POST.get('intro')
        body = request.POST.get('body')
        if category and title:
            category = Category.objects.get(pk = category)
            Post.objects.create(
                category = category,
                title = title,
                slug=slugify(title),
                intro = intro,
                body = body,
            )
            return redirect('index')

    context =  {
        # 'categories' : category,
        'form': form,
    }
    return render(request , 'newpost.html' , context)
