from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User
from django import forms
from .models import Post,Blog
class SignupForm(UserCreationForm):
	class Meta:
		model=User
		fields=['username','first_name','last_name','email']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"
