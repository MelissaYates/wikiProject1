from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Article, RelatedArticle
from .forms import ArticleForm, UserForm, LogInForm, RelatedArticleForm


# Create your views here.
# the index view is the main page that a user sees before logging into their account
def index(request):
    return render(request, 'wikiApp/index.html', {'articles': Article.objects.all()})


def login_user(request):
    if request.method == "POST":
        logged_in_user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if logged_in_user is not None:
            login(request, logged_in_user)
            return render(request, 'wikiApp/all_wiki.html')
        else:
            messages.error(request, "Incorrect Username or Password")
            return redirect('login_user')
    context = {
        "form": LogInForm
    }
    return render(request, 'wikiApp/login_user.html', context)


def new_user(request):
    if request.method == "POST":
        new_form = UserForm(request.POST)
        if new_form.is_valid():
            logged_in_user = User.objects.create_user(username=request.POST['username'],
                                                      password=request.POST['password'], )
            login(request, logged_in_user)
            return redirect('index')
        else:
            context = {
                "form": UserForm(),
                "errors": new_form.errors,
            }
            return render(request, 'wikiApp/new_user.html', context)
    return render(request, 'wikiApp/new_user.html', {'form': UserForm})

#user is able their article
def edit(request, id):
    article = get_object_or_404(Article, pk=id)
    form = ArticleForm(request.POST or None, request.FILES, instance=article)
    current_user = request.user
    user_foreign_key = Article.objects.get(pk=id)
    if request.POST:
        if form.is_valid():
            # save stuff
            form.save()
            return redirect('individual_entry')
    context = {
        'article':article,
        'form':form,
        'user_foreign_key': user_foreign_key,
        'current_user': current_user,
        'user_entries':Article.objects.all()
    }
    return render(request, 'wikiApp/edit.html', context)

#user deletes their own entry
def delete_article(request, id):
    article_to_be_deleted = Article.objects.get(pk=id)
    if article_to_be_deleted is not None:
        article_to_be_deleted.delete()
    else:
        get_object_or_404()
    return HttpResponseRedirect("/all_wiki/")

#allows user to make a new entry
def new_wiki_entry(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            tempImageFile = request.FILES
            if not tempImageFile:
                tempImageFile = ''
            else:
                tempImageFile = tempImageFile['image']
            new_article = Article(title=request.POST['title'], image=tempImageFile,
                                  content=request.POST['content'], author=request.user)
            new_article.save()
        return redirect('index')

    context = {
        'form': ArticleForm(),
        #'articles_list': Article.objects.filter(author=request.user),
    }
    return render(request, 'wikiApp/new_wiki_entry.html', context)

#the user is able to see all articles they have written on this page
def all_wiki(request):
    articles_list = Article.objects.filter(author = request.user)
    context = {
        'articles_list': articles_list,
    }
    return render(request, 'wikiApp/all_wiki.html', context)


#user is able to see their individual entry and another user is able to see an article
def individual_entry(request, id):
    context = {
        'article': get_object_or_404(Article, pk=id)
    }
    return render(request, 'wikiApp/individual_entry.html', context)

#all related posts are shown when a keyword search which matches title or content is done
def related_posts(request):
    if request.method == 'POST':
        form= RelatedArticleForm(request.POST)
        if form.is_valid():
            related_article = RelatedArticle(title=request.POST['title'],text=request.POST['text'], created_on = request.POST['created_on'], related_image=request.POST['related_image'])
            related_article.save()
            return redirect('login_user')
    return render(request, 'wikiApp/related_articles.html')

#allows search to be done in search box
def search_box(request):
    if request.method == "POST":
        print(request.POST)
        query = request.POST['query']
    context={
        'lists': Article.objects.filter(title__contains=query)}
    return render(request, 'wikiApp/search.html', context)

def display_results(request):
    return None

def logout_user(request):
    logout(request)
    return redirect('index')

