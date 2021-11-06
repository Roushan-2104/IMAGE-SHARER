from django.db import models
from django.http import request
from django.views.generic import TemplateView, DetailView, FormView, DeleteView
from django.contrib import messages
from feed.forms import PostForm
from .models import Post
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.all().order_by('-id')
        return context

class PostDetailView(DetailView):
    template_name = "detail.html"
    model = Post

class AddPostView(FormView):
    template_name= "new_post.html"
    form_class = PostForm
    success_url = "/"

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        new_object = Post.objects.create(
            text=form.cleaned_data['text'],
            image = form.cleaned_data['image']
        )
        messages.add_message(self.request, messages.SUCCESS, "Your Post Is Submitted !!")
        return super().form_valid(form)

def delete_view(request, id):
    context ={}
    obj = get_object_or_404(Post, id = id)
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "delete_view.html", context)