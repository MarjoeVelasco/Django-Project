from django import forms
from .models import Post
from .models import Category
from .models import Comment


#choices = [('coding','coding'),('sports','sports'),('entertainment','entertainment')]

choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','category','body','header_image','thumbnail')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title tag'}),
            'author': forms.TextInput(attrs={'class':'form-control','value':' ','id':'user', 'type':'hidden'}),
            #'author': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(choices = choice_list,attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter body'}),            
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','body','header_image','thumbnail')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title tag'}),
            #'author': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter body'}),            
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter name'}),
            'body': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter body'}),            
        }