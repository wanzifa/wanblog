#coding:utf-8
from django.shortcuts import render
from markdown import markdown
from .models import Post, Tag
from datetime import datetime



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

    response = render(request, 'wanzi/index.html', context_dict)
    visits = int(request.COOKIES.get('visits', '1'))
    reset_last_visit_time = False
    if 'last_visit' in request.COOKIES:
        last_visit = request.COOKIES['last_visit']
        last_visit_time = datetime.strptime(last_visit[:-7], '%Y-%m-%d %H:%M:%S')

        if(datetime.now() - last_visit_time).seconds > 0:
            visits = visits + 1
            reset_last_visit_time = True
    else:
        reset_last_visit_time = True
        
    if reset_last_visit_time:
        response.set_cookie('last_visit', datetime.now())
        response.set_cookie('visits', visits)
    return response


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
        posts = Post.objects.filter(tag=tag).order_by('-date')
    context_dict['tag'] = tag
    context_dict['posts'] = posts
    return render(request, 'wanzi/tag.html', context_dict)



