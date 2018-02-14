from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-created_date') #CREIAMO UNA VARIABILE CONTENENTE I POST PUBBLICATI
    return render(request, 'blog/post_list.html', {'posts': posts})  #VISTA CHE MOSTRA A SCHERMO LA PAGINA HTML post_list E LE PASSA LA VARIABILE posts
