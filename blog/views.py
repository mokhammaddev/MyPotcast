from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Article, Category, Tag, Comment
from .forms import CommentForm, NewsletterForm


def index(request):
    articles = Article.objects.order_by('-id')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    last_article = Article.objects.order_by('-id')[:1]
    page_number = request.GET.get('page', 1)
    paginator = Paginator(articles, 3)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(1)
    ctx = {
        'articles': page_obj,
        'categories': categories,
        'tags': tags,
        'last_article': last_article,
    }
    return render(request, 'mypotcast/index.html', ctx)


def about(request):
    articles = Article.objects.all()
    summa_view = summa_article = 0
    for obj in articles:
        summa_view += obj.views
        summa_article += 1

    form = NewsletterForm()
    if request.method == 'POST':
        form = NewsletterForm(data=request.POST)
        if form.is_valid():
            form.save()
        return redirect('.')
    ctx = {
        'form': form,
        'summa_article': summa_article,
        'summa_view': summa_view,
    }
    return render(request, 'mypotcast/about.html', ctx)


def views(request, pk):
    obj = Article.objects.get(id=pk)
    obj.views += 1
    obj.save()
    return redirect(reverse('blog:detail', kwargs={'pk': pk}))


def like(request, pk):
    obj = Article.objects.get(id=pk)
    obj.like += 1
    obj.save()
    return redirect(reverse('blog:detail', kwargs={'pk': pk}))


def detail(request, pk):
    article = get_object_or_404(Article, id=pk)
    obj = Article.objects.get(id=pk)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    comments = Comment.objects.all()
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    search = request.GET.get('search')
    form = CommentForm()
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(data=request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.name = request.user.profile.full_name
                obj.save()
                return redirect('.')
        else:
            form = CommentForm(data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('.')
    if tag:
        article = article.filter(tags__title__exact=tag)
    if cat:
        article = article.filter(category__title__exact=cat)
    if search:
        article = article.filter(title__icontains=search)
    ctx = {
        'obj': obj,
        'search': search,
        'tag': tag,
        'cat': cat,
        'article': article,
        'categories': categories,
        'tags': tags,
        'form': form,
        'comments': comments,
    }
    return render(request, 'mypotcast/episode.html', ctx)


def episodes(request):
    articles = Article.objects.order_by('-id')
    tags = Tag.objects.all()
    categories = Category.objects.all()
    page_number = request.GET.get('page', 1)
    paginator = Paginator(articles, 3)
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    search = request.GET.get('search')
    if tag:
        articles = articles.filter(tag__title__exact=tag)
    if search:
        articles = articles.filter(title__icontains=search)
    if cat:
        articles = articles.filter(category__title__exact=cat)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(1)
    ctx = {
        'search': search,
        'tag': tag,
        'cat': cat,
        'articles': page_obj,
        'tags': tags,
        'categories': categories,
    }
    return render(request, 'mypotcast/episodes.html', ctx)


def footer(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    ctx = {
        'articles': articles,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'footer.html', ctx)
