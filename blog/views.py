from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts':posts})
        ## 'request' - everything received from the user via internet
        ## 'blog/post_list.html' - template file
        ## '{}' - items can be added here for use in template
        ## part before ':' is a string and needs ''

