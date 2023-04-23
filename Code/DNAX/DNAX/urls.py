from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('uploadfile', views.uploadfile, name='upload'),
    path('add-update',views.addupdate,name='add-update'),
    path('add',views.add,name='add'),
    path('delete',views.delete,name="delete"),
    path('update',views.update,name='update'),
    path('addfile',views.addfile,name='addfile'),
    path('updatefile',views.updatefile,name='updatefile'),
    path('configfile',views.configfile,name='configfile'),
    path('report',views.report,name='report'),
    path('pat',views.pat,name='pat'),
    path('test',views.test,name='test'),
    path('output',views.output,name='output'),
]