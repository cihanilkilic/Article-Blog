from django.shortcuts import render, redirect,HttpResponse, get_object_or_404
from .forms import Article_Create_Form,Comment_Form
from django.contrib import messages
from .models import Article,Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# def article_create(request):
#     form = Article_Create_Form(request.POST or None)
#     if request.method == "POST":

#         #zorluk_seviyesi = request.POST['level']
#         if form.is_valid():
#             form.instance.author = request.user
#             form.save()
#             context = {
#                 "success":"Makale Oluşturuldu",
                
#             }
#             return render(request,"post/article_create.html",context)
#         context ={
#                 "hata":"Makale Oluşturulmadı!",
#             }
#             #messages.success(request,"Makale Oluşturuldu")
#         return render(request,"post/article_create.html",context)

@login_required(login_url="home:error")
def article_create(request):
    form = Article_Create_Form(request.POST or None, request.FILES or None)
    if form.is_valid():
        article=form.save(commit=False) # Formu kayd edecek ama bir degiskene atayacak commit=False o demekdirki auto kaydetme ozum manuel kayd edecem
        article.author=request.user
        article.save()
        context ={
            "success":"Makale Oluşturuldu",
        }
        #messages.success(request,"Makale Başarıyla Oluşturuldu!")
        return render(request,"post/article_create.html",context)
    else:
        context={
        "form":form,
        #"hata":"Makale Oluşturulmadı!",
    }

    return render(request,"post/article_create.html",context)


@login_required(login_url="home:error")
def article_show(request):
    articles = Article.objects.filter(author=request.user)#.dates("-date")
    context={
        "articles":articles,
    }

    return render(request,"post/article_show.html",context)

@login_required(login_url="home:error")
def article_detail(request, id):
    articles=Article.objects.filter(id=id)
    #articles = get_object_or_404(Article,id = id)
    comments=Comment.objects.filter(article_id=id)
    context={
    "articles":articles,
    "comments":comments,

    }

    return render(request,"post/article_detail.html",context)

@login_required(login_url="home:error")
def article_update(request,id):
    article= Article.objects.filter(id=id).first()
    form=Article_Create_Form(request.POST or None, request.FILES or None,instance=article)
    if form.is_valid():
        article=form.save(commit=False) # Formu kayd edecek ama bir degiskene atayacak commit=False o demekdirki auto kaydetme ozum manuel kayd edecem
        article.author=request.user
        article.save()
        context ={
            "success":"Makale Güncellendi",
            "form":form,
        }
        #messages.success(request,"Makale Başarıyla Oluşturuldu!")
        return render(request,"post/article_update.html",context)
    else:
        context={
        "form":form,
        #"hata":"Makale Oluşturulmadı!",
    }


    return render(request,"post/article_update.html",context)


@login_required(login_url="home:error")
def article_delete(request,id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    return redirect('article:article_show')


def article(request):
    search = request.GET.get("search")
    if search:
        articles=Article.objects.filter(title__contains=search)
        context={
            "articles":articles,
        }
        return render(request,'post/article.html',context)
    else:
        articles=Article.objects.all()
        context={
            "articles":articles,
            #"error":"Aranılan Makale Bulunamadı",
        }
    return render(request,'post/article.html',context)



def addComment(request,id):
    article = get_object_or_404(Article,id=id)
    # comment_content = request.POST.get("content")
    # comment_author = request.POST.get("author")
    # new_Comment = Article(comment_content=comment_content,comment_author=comment_author)
    # new_Comment.article = article
    # new_Comment.save()

    if request.method == 'POST':

        cf = Comment_Form(request.POST or None)

        if cf.is_valid():
            comment = cf.save(commit =False)
            content = request.POST.get("content")
            comment = Comment( comment_author = request.user, comment_content = content)
            comment.article = article
            comment.save()
            context ={
            'comment_form':cf,
            }
            #return render(request,"post/article_detail.html")
            return redirect(reverse("article:article_detail",kwargs={"id":id}))
            #return render(request, 'post/article_detail.html',context)
    else:
      cf = Comment_Form()
    context ={
      'comment_form':cf,
      }
    #return render(request, 'socio / post_detail.html', context)
    return render(request,"post/article_detail.html",context)

    #return redirect(reverse("article:article_detail",kwargs={"id":id}))#baştaki bizim değişkeniimiz ikinicisi ise html den aldığımız kısım
        

