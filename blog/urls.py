from django.conf.urls import url
from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView,UpdatePostView,DeletePostView,AddCategoryView,CategoryView,CategoryListView,AddCommentView,DeleteCommentView

app_name = 'blog'

urlpatterns = [
  
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^article/(?P<pk>\d+)$', ArticleDetailView.as_view(), name='article-detail'),
    url(r'^add_post/$', AddPostView.as_view(), name='add-post'),
    url(r'^add_category/$', AddCategoryView.as_view(), name='add-category'),
    url(r'^article/edit/(?P<pk>\d+)$', UpdatePostView.as_view(), name='update-post'),
    url(r'^article/(?P<pk>\d+)/remove$', DeletePostView.as_view(), name='delete-post'),
    #url(r'^category/<str:cats>', CategoryView, name='category'),
    path('category/<str:cats>/', CategoryView, name='category'),
    #path('category-list', CategoryListView, name='category-list'),
    url(r'^category-list/$', CategoryListView, name='category-list'),
    url(r'^article/(?P<pk>\d+)/comment$', AddCommentView.as_view(), name='add-comment'),
    url(r'^comment/(?P<pk>\d+)$', DeleteCommentView.as_view(), name='delete-comment'),
]
