from django.shortcuts import render
from django.db.models import Q
from Languages.models import *

# Create your views here.
def index(request):
    posts=Post.objects.all()
    return render(request, 'Pages/index.html', locals())

def post(request, id):
    post=Post.objects.get(id=id)
    brousers=BrouserSupport.objects.filter(post_id=id)
    return render(request, 'Pages/post.html', locals())

def search(request):
    myString=request.GET.get('search', '')
    if myString:
        posts=Post.objects.filter(name__icontains=myString)
    else:
        posts=Post.objects.all()
    
    return render(request, 'Pages/search.html', locals())

def language(request, languageName):
    myString=languageName
    cat=Language.objects.filter(Q(name=languageName) | Q(parent__name=languageName))
    posts=Post.objects.filter(prortamLanguage__in=cat)
    return render(request, 'Pages/lan.html', locals())
