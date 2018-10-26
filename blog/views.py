from django.shortcuts import render
from . import models
from django.shortcuts import redirect

# 博客主页
def index(request):
    #根据主键获取对象
    #article = models.Article.objects.get(pk=1)
    articles = models.Article.objects.all()
    #return render(request, 'blog/index.html', {'hello': 'hello,Blog!1234'});
    return render(request, 'blog/index.html', {'articles': articles});


# 博客详情页面
def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article});


# 进入新增页面
def create_page(request):
    return render(request, 'blog/create_page.html');


# 进入编辑页面
def edit_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article': article});


def create_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    models.Article.objects.create(title=title, content=content)
    return redirect('/blog/index/')


def edit_action(request):
    article_id = request.POST.get('id', 'ID')
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    models.Article.objects.filter(id=article_id).update(title=title, content=content)
    return redirect('/blog/index/')


def delete_action(request, article_id):
    models.Article.objects.filter(id=article_id).delete()
    return redirect('/blog/index/')