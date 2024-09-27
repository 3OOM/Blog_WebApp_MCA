from django.shortcuts import render, redirect
from blog.models import Blog
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def index(request):
    content = {}
    content['title'] = 'Blogs'
    blogs = Blog.objects.all()
    content['blogs'] = blogs
    return render(request, 'blog/index.html', content)

def create(request):
    content = {}
    content['title'] = 'Create a new blog'
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['image']

        blog = Blog()
        blog.title = title
        blog.description = description
        blog.image = image
        blog.save()
        
        messages.success(request, 'Blog created successfully! Go to the <a href="{}">blog section</a> to view it.'.format(reverse('blog-index')))
        return redirect('blog-create')
    return render(request, 'blog/create.html', content)

def edit(request, pk):
    content = {}
    # Access a sepcific record
    blog = Blog.objects.filter(id=pk).first()
    content['title'] = 'Edit blog id ' + str(pk)
    content['blog'] = blog
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        
        blog.title = title
        blog.description = description
        blog.save()
    return render(request, 'blog/edit.html', content)

def delete(request, pk):
    content = {}
    # Access a sepcific record
    blog = Blog.objects.filter(id=pk).first()
    content['title'] = 'Delete blog id ' + str(pk)
    content['blog'] = blog
    if request.method == 'POST':
        blog.delete()
        return HttpResponseRedirect(reverse('blog-index'))
    return render(request, 'blog/delete.html', content)