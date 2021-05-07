from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib import messages


import pickle
model = pickle.load(open("model_pickle_hate","rb"))
vect = model["vect"]
classifier = model["classifier"]


# Create your views here.

def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']   
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    

class PostDetailView(DetailView):
    model = Post     

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']   

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
       

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = Post
    fields = ['title', 'content']  
    # success_url = "/" 
    # print(form.cleaned_data["content"])


    def form_valid(self, form):
        form.instance.author = self.request.user
        stri = form.cleaned_data["content"]
        input_data = [stri]
        vectorize_input_data = vect.transform(input_data)
        result = classifier.predict(vectorize_input_data)[0]
        if result == "Negative":
            messages.add_message(self.request, messages.ERROR, 'Your Post is HateFull. We Recommend you to ammend it or it may get deleted...')
        else:
            messages.add_message(self.request, messages.SUCCESS, 'Your Post is Fine.')

        # print(result)
        return super().form_valid(form)
          

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 
  

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post 
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})    

def hate(request):
    messages.add_message(request, messages.ERROR, 'Your Post is HateFull.')
    return render(request, 'blog/hate.html')        