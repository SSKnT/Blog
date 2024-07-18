from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Post, Comment
from django.urls import reverse

def about(response):
    return render(response,'My_List/about.html',{'title':'about'});

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name='My_List/home.html'
    context_object_name = 'posts'
    login_url='user_login'
    ordering=['-Date']
    paginate_by = 5

class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name='My_List/user_post.html'
    context_object_name = 'posts'
    login_url='user_login'
    paginate_by = 5
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))    
        return Post.objects.filter(Author=user).order_by('-Date')

class PostDetailWithCommentView(LoginRequiredMixin, DetailView):
    model = Post
    template_name='My_List/detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comment = Comment.objects.filter(post=post)
        context["comments"] = comment
        return context
    

class PostCreateView(LoginRequiredMixin, CreateView):
    model=Post
    fields=['Title','Content']

    def form_valid(self, form):
        form.instance.Author=self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    success_url='/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.Author:
            return True
        return False

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=Post
    fields=['Title','Content']

    def form_valid(self, form):
        form.instance.Author=self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.Author:
            return True
        return False

class CommentCreateView(LoginRequiredMixin, CreateView):
    model=Comment
    fields=['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.post = post
        return super().form_valid(form)

class CommentDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        return reverse('Detail_view', kwargs={'pk': self.object.post.pk})

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False

#cd Desktop\Django\DJ-1
#vir_env_1\Scripts\activate
