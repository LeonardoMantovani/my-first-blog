from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-created_date') #CREIAMO UNA VARIABILE CONTENENTE I POST PUBBLICATI
    return render(request, 'blog/post_list.html', {'posts': posts})  #RITORNA LA VISTA CHE MOSTRA A SCHERMO LA PAGINA HTML post_list E LE PASSA LA VARIABILE posts

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) #OTTIENI UN OGGETTO POST CON postkey(PK) UGUALE A QUELLO CHE TI E' STATO PASSATO O, SE NON ESISTE, UNA PAGINA DI ERRORE 404
    return render(request, 'blog/post_detail.html', {'post': post})

def new_post(request):
    if request.method == "POST":  #SE IL request.method E' "POST" (QUINDI E' STATO PREMUTO IL TASTO SAVE DAL FORM)
        form = PostForm(request.POST) #INSERISCI IL FORM RICEVUTO NELLA VARIABILE form
        if form.is_valid(): #SE IL FORM HA TUTTI I CAMPI COMPILATI
            post = form.save(commit = False) #SALVALO SENZA PUBLICARLO (commit = False) NELLA VARIABILE POST
            post.author = request.user #IMPOSTA COME AUTORE L'UTENTE CORRENTE
            post.published_date = timezone.now() #IMPOSTA LA DATA DI PUBLICAZIONE AD ORA
            post.save() #SALVALO E PUBBLICALO

            return redirect('post_detail', pk=post.pk) #REINDIRIZZA L'UTENTE ALLA PAGINA DEI DETTAGLI DEL POST APPENA CREATO
    else:
        form = PostForm() #ALTRIMENTI (SE NON E' GIA' STATO PREMUTO IL PULSANTE SAVE) INIZIA UN NUOVO FORM

    return render(request, 'blog/edit_post.html', {'form': form}) #MOSTRA LA PAGINA edit_post.html

def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post) #RIPETO LA PROCEDURA USATA IN new_post SOLO CHE NELLA VARIABILE form INCLUDO ANCHE L'OGGETTO post OTTENUTO CON get_object_or_404
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/edit_post.html', {'form': form})
