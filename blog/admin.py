from django.contrib import admin
from .models import Post

# Register your models here.

admin.site.register(Post) #IMPOSTA CHE IL MODELLO Post SIA GESTIBILE DALL'ADMIN
