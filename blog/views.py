from django.shortcuts import render, get_object_or_404
from .models import blog
# Create your views here.


def all_blogs(request):
    blogs = blog.objects.order_by('-date')[:2]
    return render(request, 'blog/all_blog.html', {'blogs': blogs})


def details(request, blog_id):
    blogg = get_object_or_404(blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'id': blogg})
