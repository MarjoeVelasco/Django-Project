from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from blog.models import Profile


class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','profile_pic')
        widgets = {
            'bio': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter bio'}),            
            #'profile_pic': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title tag'}),
            }


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

    def __init__ (self, *arg, **kwargs):
        super(SignUpForm, self).__init__(*arg, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'



class UserChangeForm(ModelForm):

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','last_login','is_superuser','is_staff','is_active','date_joined')

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_login = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    is_superuser = forms.CharField(widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_staff = forms.CharField(widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_active = forms.CharField(widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    date_joined = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','last_login','is_superuser','is_staff','is_active','date_joined')


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))

    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2')