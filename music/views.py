from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, InfoSource, WordsOfWisdom
# Create your views here.

def index(request):
    post  = Post.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(post, 6)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'posts': posts})

def blog_home(request):
    post = Post.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(post, 6)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/blog_home.html', {'posts': posts})

def blog_info(request, the_slug):
    obj = Post.objects.get(slug=the_slug)
    infoSources = InfoSource.objects.filter(post=obj.id)
    
    context = {
        'object': obj,
        'infoSources': infoSources
    }
    return render(request, 'blog/blog_details.html', context)

def emmanuel_tv(request):
    return render(request, 'emmanueltv/etv.html')

def test(request):
    posts = Post.objects.all()
    return render(request, 'home.html',  {'posts': posts})


def words(request):
    wisdom = WordsOfWisdom.objects.all().order_by('-id')
    obje = Post.objects.all().order_by('-id')[:7]
    page = request.GET.get('page', 1)

    paginator = Paginator(wisdom, 4)
    try:
        words = paginator.page(page)

    except PageNotAnInteger:
        words = paginator.page(1)
    except EmptyPage:
        words = paginator.page(paginator.num_pages)
    return render(request, 'blog/words.html', {'words': words, 'obje': obje})


def aboutMe(request):
    return render(request, 'blog/aboutMe.html')    