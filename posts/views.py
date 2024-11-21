from django.shortcuts import render , redirect
from posts.models import Post
from posts.models import Category
from posts.models import Comment
from django.contrib.auth.models import User
# from django.utils.text import slugify
from posts.forms import PostForm
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
    form = PostForm()
    # category = Category.objects.all()
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        
        # category = request.POST.get('category')
        # title = request.POST.get('title')
        # intro = request.POST.get('intro')
        # body = request.POST.get('body')
        # if category and title:
        #     category = Category.objects.get(pk = category)
        #     Post.objects.create(
        #         category = category,
        #         title = title,
        #         slug=slugify(title),
        #         intro = intro,
        #         body = body,
        #     )

    context =  {
        # 'categories' : category,
        'form': form,
    }
    return render(request , 'newpost.html' , context)

def editpost(request , slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST , instance = post)

        if form.is_valid():
            form.save()
            return redirect('post' , slug=post.slug)
    
    context = {
        'post' : post,
        'form': form
    }
    return render(request , 'editpost.html' , context )

def deletepost(request , slug):
    post = Post.objects.get(slug=slug)
    post.delete()
    return redirect('index')

def comments(request, slug):
    post = Post.objects.get(slug=slug)
    commentText = Comment.objects.get()
    if request.method == "POST":
        comment_text = request.POST.get('comment')  # Get the comment text from the form
        if comment_text:
            Comment.objects.create(
                post=post,
                comments=comment_text, 
                commentText = commentText # Create the new comment linked to the post
            )
            return redirect('post', slug=slug)  # Redirect back to the same post page after submitting the comment
    
    return redirect('post', slug=slug)  # Redirect in case of GET or any other method
 # Redirect back to the post page after submitting the comment

