from django.urls import path

from . import views

urlpatterns = [
    
    path("process/", views.process, name="process"),
    path("index/",views.index,name='index'),
    path("test/",views.chat_test,name='chat_test')
    
]