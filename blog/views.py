from django.shortcuts import render, redirect, get_object_or_404
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
    blog = Blog.objects.filter(id=pk).first()
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        
        blog.title = title
        blog.description = description
        if 'image' in request.FILES:
            blog.image = request.FILES['image']
        blog.save()
        
        messages.success(request, 'Blog updated successfully! Go to the <a href="{}">blog section</a> to view it.'.format(reverse('blog-index')))
        return redirect('blog-create')
        # Instead of redirecting, we'll render the same page
    
    content = {
        'title': 'Edit blog',
        'blog': blog
    }
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

def view_post(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/view_post.html', {'blog': blog})