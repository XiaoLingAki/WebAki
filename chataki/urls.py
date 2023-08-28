
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.views import serve
from index.views import home

from . import views

urlpatterns = [
    
    path("Aki/", views.process, name="process"),
    path("GPT/",views.process_gpt,name="processgpt"),
    path("Serika/",views.process_one,name="processone"),
    path("index/",views.index,name='index'),
    path("test/",views.chat_test,name='chat_test'),
    path("image/",views.image_passing,name='image'),
    path("stablediffusion/",views.stable_diffusion,name='AIdrawing')
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)