from django.shortcuts import render, reverse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages


def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', context={'posts': posts})

class PostListView(ListView):
    model = Post
    # default_template_name =  <app>/<model>_<viewtype>.html
    template_name = 'blog/home.html'
    context_object_name = 'posts'  #default = object
    ordering = ['-date_posted']
    # wysyła context "is_paginated (True/False)" oraz "page_obj"
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post

# dla klas funkcje dekoratora @login_required spełnia dziedziczenie po klasie LoginRequiredMixin
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # sprawdza czy user to autor
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        messages.error(self.request, 'You have no permission to edit this post. Please log as the author.')
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    fields = ['title', 'content']
    # gdzie przekierować po zakonczeniu?
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        messages.error(self.request, 'You have no permission to delete this post. Please log as the author.')
        return False

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AboutView(TemplateView):
    template_name = 'blog/about.html'

def about(request):
    return render(request, 'blog/about.html')
