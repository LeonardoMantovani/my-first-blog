from django import forms
from django.contrib.auth.models import User
from .models import Post

class PostForm(forms.ModelForm): #crea un form per i post usando come modello un pre-set di django

    class Meta:  #imposta il modello e i campi del form
        model = Post
        fields = ('title', 'text',)
