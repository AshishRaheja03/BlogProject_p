from django.shortcuts import render, redirect
from .models import Blog
from django.contrib.auth.models import User
from django.contrib  import messages


# Create your views here.
def blogsListView(request):
    all_blogs = Blog.objects.all()
    return render(request, 'blogApp/blogs_list.html', {'all_blogs': all_blogs})

def blogDetailView(request, blog_pk):
   blog = Blog.objects.get(pk=blog_pk)
   return render(request, 'blogApp/blog_detail.html', {'blog': blog})

def userDashboardView(request, username):
    user = User.objects.get(username=username)
    user_blogs = Blog.objects.filter(author=user)
    return render(request, 'blogApp/user_dashboard.html', {'user_blogs': user_blogs, 'username': username})

def submitBlogView(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST.get('title')
            content = request.POST.get('content')
            author = request.user
            new_blog = Blog(title=title, content=content, author=author)
            new_blog.save()
            thumbnail = request.FILES.get('thumbnail')
            if thumbnail:
                new_blog.thumbnail = thumbnail
                new_blog.save()
            messages.success(request, "Blog submitted successfully!")
            return redirect('dashboard', username=request.user.username)
        return render(request, 'blogApp/submit_blog.html')
    else:
        messages.info(request, "Please log in to submit a blog.")
        return redirect('/auth/login/')