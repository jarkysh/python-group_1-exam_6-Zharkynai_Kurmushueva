from django.views.generic import ListView, DetailView, FormView, TemplateView, View, RedirectView
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from webapp.models import UserInfo, Post
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.generic import DetailView, ListView, CreateView, UpdateView, View, DeleteView, FormView

#from webapp.models import Food, Order, OrderFood
#from webapp.forms import FoodForm, OrderForm, OrderFoodForm

class PostListView(ListView, FormView):
    model = Post
    template_name = 'post_list.html'
    #form_class = PostSearchForm


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['post'] = Post.objects.all()
        context['author'] = Author.objects.all()
        return context

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')











#class PostCreateView(authorCreateView):
   # model = Post
    #template_name = 'post_create.html'
    #form_class = PostForm

   # def get_success_url(self):
     #   return reverse('post_detail', kwargs={'pk': self.object.pk})


#class OrderDetailView(DetailView, FormView):
    #model = Order
    #template_name = 'order_detail.html'
    #form_class = OrderFoodForm


#class OrderFoodAjaxCreateView(CreateView):
   # model = OrderFood
    #form_class = OrderFoodForm

    # обработка формы без ошибок
    #def form_valid(self, form):
     #   order = get_object_or_404(Order, pk=self.kwargs.get('pk'))
       # form.instance.order = order
       # order_food = form.save()
      #  return JsonResponse({
        #    'food_name': order_food.food.name,
         #   'amount': order_food.amount,
         #   'order_pk': order_food.order.pk,
         #   'pk': order_food.pk
        #})

    # обработка формы с ошибками
    # статус 422 - UnprocessableEntity, применяется,
    # когда запрос имеет корректный формат,
    # но неподходящие по смыслу данные (например, пустые).
  #  def form_invalid(self, form):
    #    return JsonResponse({
    #        'errors': form.errors
     #   }, status='422')



