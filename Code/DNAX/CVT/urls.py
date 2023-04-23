from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('add-update',views.addupdate,name='add-update'),
    path('add',views.add,name='add'),
    path('update',views.update,name='update'),
    path('addfile',views.addfile,name='addfile'),
    path('uploadfile', views.uploadfile, name='upload'),
    # path('chat', views.chat, name='chat'),
    # path('mresponse',views.mresponse,name="response")
]