from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.

def post_list(request):
        ## 'request' - everything received from the user via internet
        ## 'blog/post_list.html' - template file
        ## '{}' - items can be added here for use in template
        ## part before ':' is a string and needs ''
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts':posts})

def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_detail.html',{'post':post})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  ## 'commit=False' means that the 'Post' model is not save yet since the author should also be added
            post.author = request.user
            post.published_date = timezone.now()
            post.save() ## preserve the change and add the author
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html',{'form':form})

def post_edit(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method =="POST":
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date=timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form =PostForm(instance=post) ## open the form for edit
    return render (request,'blog/post_edit.html',{'form':form})
