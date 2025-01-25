from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.

def post_list(request):
    all_posts = Post.objects.all()
    return render (request, 'post/post_list.html', {'all_posts':all_posts})

def post_details(request, id):
    post = Post.objects.get(id=id)
    return render (request, 'post/post_detail.html', {'post':post})


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    return render(request, 'post/post_create.html',{'form':form})

def post_edit(request, id):
    post= Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
    else:
        form = PostForm(instance=post)
    return render(request, 'post/post_edit.html',{'form':form})




class PostList(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'all_posts'

class PostDetail(DetailView):
    pass
    model =Post
    template_name = 'post/post_detail.html'
    context_object_name = 'post'

class CreatePost(CreateView):
    model = Post
    template_name = 'post/post_create.html'
    fields= '__all__'
    success_url = reverse_lazy('success_url')
    