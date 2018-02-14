from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list') #SE NON VIENE AGGIUNTO NESSUN URL ALL'INDIRIZZO PRINCIPALE MOSTRA LA VISTA post_list
]
