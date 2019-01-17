from django.shortcuts import render, redirect, get_object_or_404#,reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, View, RedirectView,CreateView,UpdateView, DeleteView
from webapp.models import *
from django.urls import reverse_lazy
from webapp.forms import *
import datetime

class IndexView(TemplateView):
    template_name = 'index.html'
    context_object_name = 'post_list'


def get_context_date(self, **kwargs):
    context = super().get_context_date(**kwargs)
    return context

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    form_class = ProjectSearchForm

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        else:
            return super().dispatch(request, *args, **kwargs)


    def get_queryset(self):
         return Post.objects.all().order_by('date').reverse()

    def get_queryset(self):
        search_string = self.request.GET.get('search_string')
        if search_string:
            return self.model.objects.filter(post__icontains=search_string) | \
                   self.model.objects.filter(text__icontains=search_string)
        else:
            return self.model.objects.all()


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm
    success_url = reverse_lazy('post_list')

def post_create_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'post_create.html')
        else:
            return redirect('login')

    elif request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        author = request.user
        date = datetime.datetime.now()
        Post.objects.create(title=title, text=text, author=author,date=date)
        return redirect('post_list')



class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_update.html'
    success_url = reverse_lazy('post_list')

    def post_update_view(request):
        if request.method == 'GET':
            if request.user.is_authenticated:
                return render(request, 'post_update.html')
            else:
                return redirect('login')

        elif request.method == 'POST':
            title = request.POST.get('title')
            text = request.POST.get('text')
            author = request.user
            date = datetime.datetime.now()
            Post.objects.create(title=title, text=text, author=author, date=date)
            return redirect('post_list')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')

def post_delete_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if not request.user.is_authenticated:
        return redirect('login')
    elif request.user == post.author:
        if request.method == 'GET':
            return render(request, 'post_delete.html', context={
                'post': post
            })
        elif request.method == 'POST':
            if request.POST.get('delete') == 'yes':
                post.delete()
            return redirect('../')
    else:
        return redirect('../post/'+str(pk))

class UserListView(ListView):
    model = UserInfo
    template_name = 'user_list.html'

class UserDetailView(DetailView):
    model = UserInfo
    template_name = 'user_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('date').reverse()
        return context

class UserUpdateView(UpdateView):
    model = UserInfo
    form_class = UserForm
    template_name = 'user_update.html'
    success_url = reverse_lazy('user_list')

class UserDeleteView(DeleteView):
        model = UserInfo
        fields = ['phone', 'image']
        form_class = UserForm
        template_name = 'user_delete.html'
        success_url = reverse_lazy('user_list')




# Create your views here.


