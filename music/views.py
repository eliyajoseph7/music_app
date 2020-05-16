from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    return render(request, 'index.html')

def videos_image(request):
    posts = Post.objects.all()
    # context = {
    #     'title': obj.title,
    #     'image': obj.image
    # }
    return render(request, 'videos.html', {'posts': posts})

def video_infos(request, the_slug):
    obj = Post.objects.get(slug=the_slug)
    context = {
        'object': obj
    }
    return render(request, 'video.html', context)

def emmanuel_tv(request):
    return render(request, 'emmanueltv/etv.html')