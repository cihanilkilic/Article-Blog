from django.shortcuts import render
from article.models import Article
from django.contrib.auth.models import User
import datetime

def index (request):
    articles = Article.objects.all()#.dates("-date")
    context={
        "articles":articles,
    }
    return render(request,"home/index.html",context)

def about (request):
    return render(request,"about/about.html")


def contact (request):
    return render(request,"contact/contact.html")



def error (request):
    return render(request,"error/error.html")