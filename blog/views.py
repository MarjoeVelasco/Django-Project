from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from .models import Post
from .models import Category
from .models import Comment
from .forms import PostForm
from .forms import EditForm
from .forms import CommentForm
from django.urls import reverse_lazy
from django.urls import reverse


class HomeView(ListView):
    paginate_by = 3
    model = Post
    template_name = 'home.html'
    #ordering = ['-id']
    ordering = ['-id']


    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html',{'cat_menu_list':cat_menu_list})

def CategoryView(request, cats):
    category_post = Post.objects.filter(category=cats)
    return render(request, 'categories.html',{'cats':cats.title(), 'category_post':category_post})



class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html' 

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    #fields = ('title','body')

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    #fields = '__all__'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk'] 
        return super().form_valid(form)
    
    def get_success_url(self):
         #print(self.pk)
         return reverse('blog:article-detail', kwargs={'pk': self.kwargs['pk']})

    #success_url = reverse_lazy('blog:home')

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'
    #fields = ('title','body')

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title','title_tag','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    #fields = ['title','title_tag','body']
    success_url = reverse_lazy('blog:home')

class DeleteCommentView(DeleteView):
    model = Comment
    template_name = 'delete_comment.html'
    
    
    #fields = ['title','title_tag','body']
    #success_url = reverse_lazy('blog:home')
    
    def get_success_url(self):
        #print(self.pk)
        comment_id = self.kwargs['pk'] 
        comment = Comment.objects.get(pk=comment_id)
        post_id = comment.post.id
        return reverse('blog:article-detail', kwargs={'pk': post_id})

    
