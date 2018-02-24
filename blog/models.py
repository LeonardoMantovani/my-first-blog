from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User') #RIMANDA A UN ALTRO MODELLO
    title = models.CharField(max_length=200) #CAMPO TESTO CON LETTERE LIMITATE
    text = models.TextField() #CAMPO TESTO INFINITO
    created_date = models.DateTimeField(default=timezone.now) #CAMPO DATA-ORA
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self): #METODO PER LA PUBLICAZIONE DEL POST
        self.published_date = timezone.now()
        self.save()

    def __str__(self): #METODO CHE RESTITUISCE IL TITOLO DEL POST
        return self.title
