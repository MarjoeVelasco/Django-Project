from django.conf.urls import url
from django.urls import path
from .views import UserRegisterView,UserEditView,PasswordsChangeView,ShowProfilePageView,EditProfilePageView,CreateProfilePageView
from django.contrib.auth import views as auth_views
from . import views

app_name = 'members'

PasswordsChangeView
urlpatterns = [
    url('^register$', UserRegisterView.as_view(), name='register'),
    url('^login$', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    url('^edit_profile$', UserEditView.as_view(), name='edit-profile'),
    #url('^password$', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    #url(r'^password$', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html'), name='change-password'),
    path('password_success', views.password_success, name='password-success'),
    url(r'^(?P<pk>\d+)/profile/$', ShowProfilePageView.as_view(), name='show-profile-page'),
    url(r'^(?P<pk>\d+)/edit_profile_page/$', EditProfilePageView.as_view(), name='edit-profile-page'),
    #path('<int:pk>/profile/', ShowProfilePageView.as_view, name='show-profile-page'),
    url('^create_profile_page$', CreateProfilePageView.as_view(), name='create-profile-page'),

]
