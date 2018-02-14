from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')), #PER TUTTI GLI URL CHE NON SONO QUI SOPRA SEGUI LE ISTRUZIONI DI blog.urls
]
