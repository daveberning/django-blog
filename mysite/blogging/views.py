from django.shortcuts import render
from django.http import Http404
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class PostDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'

    def get(self, request, *args, **kwargs):
        published = Post.objects.exclude(published_date__exact=None)
        try:
            post = published.get(pk=self.kwargs['post_id'])
        except Post.DoesNotExist:
            raise Http404
        return render(request, 'blogging/detail.html', {'post': post})


class PostListView(ListView):
    model = Post
    template_name = 'blogging/list.html'
    queryset = Post.objects.exclude(published_date__exact=None).order_by('-published_date')

    def get(self, request, *args, **kwargs):
        posts = Post.objects.exclude(published_date__exact=None).order_by('-published_date')
        return render(request, 'blogging/list.html', {'posts': posts})