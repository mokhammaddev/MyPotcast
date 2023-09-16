from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from blog.models import Article, Tag, Category
from profile.models import Profile


def blog(request):
    articles = Article.objects.order_by('-id')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    author = Profile.objects.get()
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    search = request.GET.get('search')
    if tag:
        articles = articles.filter(tag__title__exact=tag)
    if cat:
        articles = articles.filter(category__title__exact=cat)
    if search:
        articles = articles.filter(title__icontains=search)
    page_number = request.GET.get('page', 1)
    paginator = Paginator(articles, 2)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(1)
    ctx = {
        'tag': tag,
        'cat': cat,
        'search': search,
        'articles': page_obj,
        'categories': categories,
        'tags': tags,
        'author': author,
    }
    return render(request, 'mypotcast/blog.html', ctx)
