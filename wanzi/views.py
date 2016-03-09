#coding:utf-8
from django.shortcuts import render
from markdown import markdown
from .models import Post, Tag



def index(request):
    context_dict = {}
    count = Tag.objects.count()
    count1 = count/2
    tag1 = Tag.objects.all()[:count1]
    tag2 = Tag.objects.all()[count1:]
    context_dict['tag1'] = tag1
    context_dict['tag2'] = tag2
    if request.method == 'POST':
        query = request.POST['query']
        posts = [post for post in Post.objects.all() if query.lower() in post.title.lower()]
        context_dict['posts'] = posts
        return render(request, 'wanzi/search.html', context_dict)
    return render(request, 'wanzi/index.html', context_dict)


def about(request):
    return render(request, 'wanzi/about.html')


def blogs(request):
    context_dict = {}
    posts = Post.objects.order_by('-date')
    context_dict['posts'] = posts
    return render(request, 'wanzi/blogs.html', context_dict)


def post(request, post_name):
    context_dict = {}
    if request.method == 'GET':
        post = Post.objects.get(title=post_name)
    context_dict['post'] = post
    return render(request, 'wanzi/blog.html', context_dict)


def tag(request, tag_name):
    context_dict = {}
    tag = Tag.objects.get(name=tag_name)
    if request.method == 'GET':
        posts = Post.objects.filter(tag=tag)
    context_dict['tag'] = tag
    context_dict['posts'] = posts
    return render(request, 'wanzi/tag.html', context_dict)



