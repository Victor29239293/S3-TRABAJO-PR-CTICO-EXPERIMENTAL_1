from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        q = self.request.GET.get('q', '').strip()
        if q:
            return Post.objects.filter(title__icontains=q).order_by('-created_at')
        return Post.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context
    
class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = False
        return context

class PostUpdateView(UpdateView):
    model = Post 
    template_name = 'blog/form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['is_update'] = True
        return context
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/confirm_delete.html'
    success_url = reverse_lazy('post_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    reverse_lazy = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



