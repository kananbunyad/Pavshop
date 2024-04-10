from django.shortcuts import render,redirect
from django.contrib import messages
# from django.http import HttpResponse
from blog.forms import CommentForm
from blog.models import Blog,BlogCategory,BlogTag





def blog(request):
    blog = Blog.objects.all()
    categories=BlogCategory.objects.all()
    tags=BlogTag.objects.all()
    context = {
        'blogs': blog,
        'categories': categories,
        'tags' : tags
    }
    return render(request, 'blog-list.html',context=context)


def blog_detail(request,slug):
    form = CommentForm()
    blog_detail = Blog.objects.get(slug = slug)
    blog_detail.view_count+=1
    blog_detail.save()
    categories=BlogCategory.objects.all()
    tags=BlogTag.objects.all()
    if request.method == "POST":
        form = CommentForm(data=request.POST)
      
        if form.is_valid():
            user= form.save(commit=False)
            user.blog_id=blog_detail
            user.user_id=request.user
            user.save()
            messages.add_message(request, messages.SUCCESS, "Comment sent successfully")
            return redirect('blog:blog-detail',slug=slug)

    context = {
        'blog': blog_detail,
        'form' : form,
        'categories': categories,
        'tags' : tags

    }
    return render(request, 'blog-detail.html',context=context)

