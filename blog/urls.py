from django.conf.urls import url
from django.contrib.auth import views as djangoauth_views
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'), #SE NON VIENE AGGIUNTO NESSUN URL ALL'INDIRIZZO PRINCIPALE MOSTRA LA VISTA post_list
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'), #CREA UNA URL PER OGNI POST CHE CONSISTE IN indirizzodelsito.com/post/<post_id> CON AL POSTO DI <post_id> UN NUMERO ASSEGNATO AL POST
    url(r'^post/new/$', views.new_post, name='new_post'), #CREA UNA URL PER IL FORM DI CREAZIONE DEI POST
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.edit_post, name='edit_post'),
    url(r'^register/$', views.singup, name='singup'),
    url(r'^login/$', djangoauth_views.login, {'template_name': 'blog/login.html'}, name='login'),
    url(r'^logout/$', djangoauth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^post/(?P<pk>[0-9]+)/remove/$', views.remove_post, name='remove_post'),
]
