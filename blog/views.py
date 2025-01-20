from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from blog.models import Blog
from django.urls import reverse_lazy, reverse


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        return Blog.objects.filter(is_published=False)


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'image')
    success_url = reverse_lazy('blog:blog_list')


class BlogDetailView(DetailView):
    model = Blog

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content')
    success_url = reverse_lazy('blog:blog_list')

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')


class ContactView(TemplateView):
    template_name = 'blog/contacts.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
