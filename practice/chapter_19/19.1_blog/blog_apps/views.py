from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Blog, Article
from .form import ArticleForm, BlogForm

# Create your views here.
def blogs(request):
    """main page function"""
    blogs = Blog.objects.order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blog_apps/blogs.html', context)


def blog(request, blog_id):
    """show one's blog and articles"""
    blog = Blog.objects.get(id=blog_id)
    articles = blog.article_set.order_by('-date_added')
    context = {'blog': blog, 'articles': articles}
    return render(request, 'blog_apps/blog.html', context)

@login_required
def new_blog(request):
    """add new blog"""
    if request.method != 'POST':
        # Don't submit data: create a new form
        form = BlogForm()
    else:
        # Submit data by POST: process the data
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_apps:blogs')

    # Show empty form or indicate that the form is invalid
    context = {'form': form}
    return render(request, 'blog_apps/new_blog.html', context)

@login_required
def new_article(request, blog_id):
    """Add new article in specific blog"""
    blog = Blog.objects.get(id=blog_id)
    if request.method != 'POST':
        form = ArticleForm()
    else:
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.blog = blog
            new_article.owner = request.user
            new_article.save()
            return redirect('blog_apps:blog', blog_id=blog_id)

    context = {'blog': blog, 'form': form}
    return render(request, 'blog_apps/new_article.html', context)

@login_required
def edit_article(request, article_id):
    """Edit article which had been submitted"""
    article = Article.objects.get(id=article_id)
    blog = article.blog

    if request.user != article.owner:
        raise Http404

    if request.method != 'POST':
        # First request: Using current article fill form.
        form = ArticleForm(instance=article)
    else:
        # The data submitted by POST: Porcessing data.
        form = ArticleForm(instance=Article, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_apps:blog', blog_id=blog.id)
    
    context = {'article': article, 'blog': blog, 'form': form}
    return render(request, 'blog_apps/edit_article.html', context)